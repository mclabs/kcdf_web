import os, sys
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
#sys.path.append('/usr/local/lib/python2.6/dist-packages/django/')
sys.path.append('/usr/lib/python2.6/site-packages/django/')
sys.path.append('/home/kcdfweb/webapps/kcdf.or.ke/releases/current/kcdf')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kcdf.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
