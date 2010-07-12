from django.conf.urls.defaults import *
urlpatterns=patterns('',
		(r'^search/', include('haystack.urls')),

	)


urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^rss/$', 'flatpage', {'url': '/rss/'}, name='rss'),
    url(r'^donate/$', 'flatpage', {'url': '/donate/'}, name='donate'),
    url(r'^education-partners/$', 'flatpage', {'url': '/education-partners/'}, name='partners'),
    url(r'^take-action-education/$', 'flatpage', {'url': '/take-action-education/'}, name='take-action'),

)

urlpatterns+=patterns('arts.views',
		(r'^$', 'index',{},'home'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		(r'^case-study/(?P<slug>[^\.^/]+)/$', 'casestudy_detail',{},'casestudy'),
		(r'^news/(?P<slug>[^\.^/]+)/$', 'news_detail',{},'news'),
		(r'^news/$', 'news',{},'news'),
		(r'^resource/(?P<slug>[^\.^/]+)/$', 'resource_detail',{},'resource'),
		(r'^events/(?P<slug>[^\.^/]+)/$', 'events_detail',{},'events'),
		(r'^events/$', 'events',{},'events'),
		(r'^page/about-arts/$', 'page',{},'about-arts'),
		(r'^resource-center/$', 'resources',{},'resource-center'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'inner_page',{},'about-arts'),


)