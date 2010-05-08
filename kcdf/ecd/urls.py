from django.conf.urls.defaults import *
urlpatterns= patterns('django.contrib.flatpages.views',
    url(r'^rss/$', 'flatpage', {'url': '/rss/'}, name='rss'),
    url(r'^donate/$', 'flatpage', {'url': '/donate/'}, name='donate'),
    url(r'^ecd-partners/$', 'flatpage', {'url': '/ecd-partners/'}, name='partners'),
    url(r'^take-action-ecd/$', 'flatpage', {'url': '/take-action-ecd/'}, name='take-action'),

)
urlpatterns+=patterns('ecd.views',
		(r'^$', 'index',{},'home'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		(r'^case-study/(?P<slug>[^\.^/]+)/$', 'casestudy_detail',{},'casestudy'),
		(r'^news/(?P<slug>[^\.^/]+)/$', 'news_detail',{},'news'),
		(r'^news/$', 'news',{},'news'),
		(r'^resource/(?P<slug>[^\.^/]+)/$', 'resource_detail',{},'resource'),
		(r'^resource-center/$', 'resources',{},'resource-center'),


)