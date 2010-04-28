from django.conf.urls.defaults import *
urlpatterns=patterns('ustawi.views',
		(r'^$', 'index',{},'home'),
)