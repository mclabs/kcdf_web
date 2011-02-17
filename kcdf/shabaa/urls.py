from django.conf.urls.defaults import *

urlpatterns=patterns('',
		(r'^search/', include('haystack.urls')),

	)

urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^rss/$', 'flatpage', {'url': '/rss/'}, name='rss'),
    url(r'^donate/$', 'flatpage', {'url': '/donate/'}, name='donate'),
    url(r'^shabaa-partners/$', 'flatpage', {'url': '/shabaa-partners/'}, name='partners'),
    url(r'^take-action-shabaa/$', 'flatpage', {'url': '/take-action-shabaa/'}, name='take-action'),

)

urlpatterns+=patterns('shabaa.views',
		(r'^$', 'index',{},'home'),
		(r'^case-studies/$', 'case_studies',{},'case-studies'),
		(r'^case-study/(?P<slug>[^\.^/]+)/$', 'casestudy_detail',{},'casestudy'),
		(r'^news/(?P<slug>[^\.^/]+)/$', 'news_detail',{},'news'),
		(r'^news/$', 'news',{},'news'),
		(r'^resource/(?P<slug>[^\.^/]+)/$', 'resource_detail',{},'resource-center'),
		(r'^resource-center/$', 'resources',{},'resource-center'),
		(r'^events/(?P<slug>[^\.^/]+)/$', 'events_detail',{},'events'),
		(r'^events/$', 'events',{},'events'),
		(r'^page/about-shabaa/$', 'page',{},'about-shabaa'),
		(r'^page/(?P<slug>[^\.^/]+)/$', 'inner_page',{},'about-shabaa'),
		(r'^funders/$', 'funders',{},'funders'),
		(r'^legal-documents/$', 'legal_docs',{},'legal'),
		(r'^individual-registration/$', 'indiv_reg',{},'individual'),
		(r'^business-registration/$', 'business_reg',{},'business'),
		(r'^service-providers/$', 'service_prov',{},'service'),
		(r'^youth-programs/$', 'youth_prog',{},'youth'),

		(r'^funder/(?P<slug>[^\.^/]+)/$', 'funders_detail',{},'funders'),
		(r'^legal-document/(?P<slug>[^\.^/]+)/$', 'legal_detail',{},'legal'),
		(r'^individual-registration/(?P<slug>[^\.^/]+)/$', 'indiv_detail',{},'individual'),
		(r'^business-registration/(?P<slug>[^\.^/]+)/$', 'business_detail',{},'business'),
		(r'^service-provider/(?P<slug>[^\.^/]+)/$', 'service_detail',{},'service'),
		(r'^pdf/(?P<slug>[^\.^/]+)/$', 'print_pdf',{},'business'),

)