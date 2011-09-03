from django.conf.urls.defaults import *
urlpatterns=patterns('',
		(r'^search/', include('haystack.urls')),

	)

urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^rss/$', 'flatpage', {'url': '/rss/'}, name='rss'),
    url(r'^donate/$', 'flatpage', {'url': '/donate/'}, name='donate'),
    url(r'^ustawi-partners/$', 'flatpage', {'url': '/ustawi-partners/'}, name='partners'),
    url(r'^take-action-ustawi/$', 'flatpage', {'url': '/take-action-ustawi/'}, name='take-action'),

)

urlpatterns+=patterns('ustawi.views',
		(r'^$', 'index',{},'home'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		(r'^case-study/(?P<slug>[^\.^/]+)/$', 'casestudy_detail',{},'casestudy'),
		(r'^news/(?P<slug>[^\.^/]+)/$', 'news_detail',{},'news'),
		(r'^news/$', 'news',{},'news'),
		(r'^resource/(?P<slug>[^\.^/]+)/$', 'resource_detail',{},'resource'),
		(r'^events/(?P<slug>[^\.^/]+)/$', 'events_detail',{},'events'),
		(r'^events/$', 'events',{},'events'),
		(r'^page/about-ustawi/$', 'page',{},'about-ustawi'),
		(r'^resource-center/$', 'resources',{},'resource-center'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'inner_page',{},'about-ustawi'),
		(r'^grantees/(?P<sYear>\d{4})/(?P<eYear>\d{4})/$', 'grantees_by_year',{},'grantees'),
		(r'^grantees/$','grantees_by_year',{},'grantees'),
                 (r'^videos/$', 'videos',{},'videos'),
		(r'^video/(?P<slug>[^\.^/]+)/$', 'video_details',{},'videos'),
		(r'^downloads/$', 'downloads',{},'downloads'),
		(r'^downloads/(?P<slug>[^\.^/]+)/$', 'download_details',{},'downloads'),
		(r'^audios/$', 'audios',{},'audios'),
		(r'^audio/(?P<slug>[^\.^/]+)/$', 'audio_details',{},'audios'),


)
