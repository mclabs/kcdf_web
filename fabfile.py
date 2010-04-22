# globals
from fabric.api import env, local, run, sudo, put, cd, runs_once, prompt, require, settings
from fabric.contrib.files import exists, upload_template
from fabric.contrib.console import confirm
from fabric.context_managers import hide

env.project_name = 'kcdf'
env.project_domain = 'kcdf.or.ke' # Project domain

# environments

def production():
    "Use the local virtual server"
    env.hosts = ['173.203.124.16']
    env.path = '/home/kcdfweb/webapps/kcdf.or.ke'
    env.user = 'kcdfweb'
    #env.password ='wb56829hef'
    env.virtualhost_path = "apache"
    #env.shell = '/usr/local/bin/bash -l -c' # Path to your shell binary
    env.sudo_prompt = 'Password:' # Sudo password prompt
    env.warn_only = True
    env.www_user = 'www-data' # User account under which Apache is running

# tasks

def test():
    "Run the test suite and bail out if it fails"
    local("cd $(project_name); python manage.py test", fail="abort")

def setup():
    """
    Setup a fresh virtualenv as well as a few useful directories, then run
    a full deployment
    """
    require('hosts', provided_by=[production])
    require('path')
    
    sudo('aptitude install -y python-setuptools')
    sudo('easy_install pip')
    #sudo('pip install virtualenv')
    sudo('aptitude install -y apache2')
    sudo('aptitude install -y libapache2-mod-wsgi')

    # we want rid of the defult apache config
    #sudo('cd /etc/apache2/sites-available/; a2dissite default;')
    #sudo('mkdir -p %(path)s; cd %(path)s; virtualenv --no-site-packages .'  % {'path': env.path})
    sudo('mkdir -p %(path)s;'  % {'path': env.path})

    sudo('chown -R %(user)s:%(user)s %(path)s'  % {'user': env.user, 'path': env.path})
    run('cd %(path)s; mkdir releases; mkdir packages' % {'path': env.path})
    deploy()

def deploy():
    """
    Deploy the latest version of the site to the servers, install any
    required third party modules, install the virtual host and 
    then restart the webserver
    """
    require('hosts', provided_by=[production])
    require('path')

    import time
    env.release = time.strftime('%Y%m%d%H%M%S')

    upload_tar_from_git()
    install_requirements()
    install_site()
    symlink_current_release()
    migrate()
    restart_webserver()

def deploy_version(version):
    "Specify a specific version to be made live"
    require('hosts', provided_by=[production])
    require('path')
    
    env.version = version
    run('cd %(path); rm releases/previous; mv releases/current releases/previous;')
    run('cd %(path); ln -s $(version) releases/current')
    restart_webserver()

def rollback():
    """
    Limited rollback capability. Simple loads the previously current
    version of the code. Rolling back again will swap between the two.
    """
    require('hosts', provided_by=[production])
    require('path')

    run('cd $(path); mv releases/current releases/_previous;')
    run('cd $(path); mv releases/previous releases/current;')
    run('cd $(path); mv releases/_previous releases/previous;')
    restart_webserver()
    
# Helpers. These are called by other functions rather than directly

def upload_tar_from_git():
    require('release', provided_by=[deploy, setup])
    "Create an archive from the current Git master branch and upload it"
    '''
    local('hg archive --type=tar $(release).tar.gz')
    run('mkdir $(path)/releases/$(release)')
    put('$(release).tar.gz', '$(path)/packages/')
    run('cd $(path)/releases/$(release) && tar zxf ../../packages/$(release).tar.gz')
    local('rm $(release).tar.gz')
    '''
    local('git archive --format=tar master > %(release)s.tar' % {'release': env.release})
    run('mkdir %(path)s/releases/%(release)s' % {'path': env.path, 'release': env.release})
    put('%(release)s.tar' % {'release': env.release}, '%(path)s/packages/' % {'path': env.path})
    run('cd %(path)s/releases/%(release)s && tar xf ../../packages/%(release)s.tar' % {'path': env.path, 'release': env.release})
    #on windows we use del on linux rm
    local('del %(release)s.tar' % {'release': env.release})


def install_site():
    "Add the virtualhost file to apache"
    require('release', provided_by=[deploy, setup])
    with cd('%(path)s/releases/%(release)s' % env):
	sudo('cp %(project_name)s/%(virtualhost_path)s/%(project_domain)s /etc/apache2/sites-available/%(project_domain)s' % env)
    with cd('/etc/apache2/sites-available'):
	sudo('a2ensite %(project_domain)s' % env) 
    sudo('chown -R %(www_user)s:%(www_user)s %(path)s/releases/%(release)s' % {'www_user': env.www_user, 'path': env.path, 'release': env.release})

def install_requirements():
    "Install the required packages from the requirements file using pip"
    require('release', provided_by=[deploy, setup])
    #with cd('%(path)s;' % env):
	#sudo('pip install -r ./releases/%(release)s/requirements.txt' % env)
    run('cd %(path)s; sudo pip install -r ./releases/%(release)s/requirements.txt' % {'path': env.path, 'release': env.release})


def symlink_current_release():
    "Symlink our current release"
    require('release', provided_by=[deploy, setup])
    #run('cd %(path)s; rm releases/previous; mv releases/current releases/previous;' % {'path': env.path }) 
    #run('cd %(path)s; ln -s %(release)s releases/current' % {'path': env.path, 'release': env.release})
    with settings(hide('warnings', 'stderr'), warn_only = True):
        run('cd %(path)s; rm releases/previous; mv releases/current releases/previous' % {'path': env.path }) 
	#run('cd %(path)s; mkdir admin_media' % {'path': env.path })
	#run('cd %(path)s; ln -s /usr/local/lib/python2.6/dist-packages/django/contrib/admin/media/ admin_media' % {'path': env.path })
    run('cd %(path)s; ln -s %(release)s releases/current' % {'path': env.path, 'release': env.release})



def migrate():
    "Update the database"
    require('project_name')
    #run('cd %(path)/releases/current/%(project_name);  ../../../bin/python manage.py syncdb --noinput' % {'path': env.path, 'release': env.release,'project_name':env.project_name})
    run('cd %(path)s/releases/current/%(project_name)s; python manage.py syncdb --noinput' % {'path': env.path,'project_name': env.project_name})

def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 reload')


