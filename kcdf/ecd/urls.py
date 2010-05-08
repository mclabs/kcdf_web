from django.conf.urls.defaults import *
urlpatterns=patterns('ecd.views',
		(r'^$', 'index',{},'home'),
)