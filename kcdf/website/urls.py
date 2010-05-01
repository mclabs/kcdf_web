from django.conf.urls.defaults import *
from website.feeds import LatestNews
from website.models import News,Program
from django.contrib import admin
admin.autodiscover()


info_dict = {
    'queryset': Program.objects.all(),
}


feeds = {
    'news': LatestNews,
}
urlpatterns=patterns('',
		(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
		{'feed_dict': feeds}),
		(r'^admin/', include(admin.site.urls)),
		(r'^admin/filebrowser/', include('filebrowser.urls')),

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
		(r'^resource/(?P<slug>[^\.^/]+)/$', 'resource_detail',{},'resource'),
		(r'^partners/$', 'page',{},'partners'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'page',{},'page'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'page',{},'page'),
		(r'^news/(?P<slug>[^\.^/]+)/$', 'news_detail',{},'news'),
		(r'^news/$', 'news',{},'news'),

)
