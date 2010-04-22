from django.conf.urls.defaults import *
from website.feeds import LatestNews

feeds = {
    'news': LatestNews,
}
urlpatterns=patterns('',
		(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
		{'feed_dict': feeds}),
	)

urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^rss/$', 'flatpage', {'url': '/rss/'}, name='rss'),
    url(r'^donate/$', 'flatpage', {'url': '/donate/'}, name='donate'),
    url(r'^partners/$', 'flatpage', {'url': '/partners/'}, name='partners'),
    url(r'^take-action/$', 'flatpage', {'url': '/take-action/'}, name='take-action'),

)
urlpatterns += patterns('kcdf.website.views',
		(r'^$', 'index',{},'home'),
		(r'^programs/$', 'programs',{},'programs'),
		(r'^program/(?P<slug>[^\.^/]+)/$', 'program_details',{},''),
		(r'^resource-center/$', 'resources',{},'resource-center'),
		(r'^partners/$', 'page',{},'partners'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'page',{},'page'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		
)
