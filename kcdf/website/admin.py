from django.contrib import admin
from website.models import *
from shabaa.models import *
from website.forms import AdminImageForm
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

	

		

class CaseStudyAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','title','program','slug','tags')
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(CaseStudyAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'long_description':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field

class NewsAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','title','program','slug','tags')
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'long_description':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field

class EventsAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','title','program','slug','tags')
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(EventsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'long_description':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field


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
	list_display = ('id','title','program','slug','tags')
	exclude=('slug',)
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(ResourceAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'long_description':
			return forms.CharField(widget=TinyMCE(
			attrs={'cols': 80, 'rows': 30}))
		return field


class HeadlineAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	form = AdminImageForm
	exclude=('slug',)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	exclude=('slug',)

class AudioAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	exclude=('slug',)

class DownloadsAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	exclude=('slug',)


class GranteeAdmin(admin.ModelAdmin):
	list_display = ('id','name','program','amount','slug')
	exclude=('slug',)

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('id','name','email')

admin.site.register(Headline,HeadlineAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Resource,ResourceAdmin)
admin.site.register(ResourceType)
admin.site.register(CaseStudy,CaseStudyAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Events,EventsAdmin)
admin.site.register(Page,PageAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Downloads,DownloadsAdmin)
admin.site.register(Stats)
admin.site.register(Location)
admin.site.register(ProjectPartner)
admin.site.register(Grantee,GranteeAdmin)
admin.site.register(Audio,AudioAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
