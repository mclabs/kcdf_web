from django.conf.urls.defaults import *
from django.conf import settings
from kcdf.website.models import News,Program

info_dict = {
    'queryset': Program.objects.all(),
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^', include('website.urls')),
    (r'^', include('ustawi.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    # Example:
    # (r'^kcdf/', include('kcdf.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     #(r'^admin/(.*)', admin.site.root),
)
