from django.conf.urls.defaults import *
urlpatterns=patterns('',
		(r'^search/', include('haystack.urls')),

	)


urlpatterns+= patterns('django.contrib.flatpages.views',
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
		(r'^events/(?P<slug>[^\.^/]+)/$', 'events_detail',{},'events'),
		(r'^events/$', 'events',{},'events'),
		(r'^page/about-ecd/$', 'page',{},'about-ecd'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'inner_page',{},'about-ecd'),
		(r'^grantees/(?P<sYear>\d{4})/(?P<eYear>\d{4})/$', 'grantees_by_year',{},'grantees'),


)