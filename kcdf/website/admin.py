from django.contrib import admin
from website.models import *

from django import forms
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

	
class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	exclude=('slug',)
	search_fields = ['id', 'title']
	search_fields_verbose = ['ID', 'Title']

		

class CaseStudyAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug')

class NewsAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','title','slug','tags')

class EventsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug')

class PageAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug','parent')
	exclude=('slug',)
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'content':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field


class ProgramAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	exclude=('slug',)
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(ProgramAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'description':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field
	

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Headline)

admin.site.register(Program,ProgramAdmin)
admin.site.register(Resource,ResourceAdmin)
admin.site.register(ResourceType)
admin.site.register(CaseStudy,CaseStudyAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Events,EventsAdmin)
admin.site.register(Page,PageAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
