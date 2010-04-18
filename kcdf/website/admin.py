from django.contrib import admin
from website.models import *
	
class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug')

	search_fields = ['id', 'title']
	search_fields_verbose = ['ID', 'Title']

		

class CaseStudyAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug')

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug','tags')

class EventsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id','title','slug')

class PageAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug','parent')
	prepopulated_fields = {"slug": ("title",)}

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug')
	prepopulated_fields = {"slug": ("title",)}

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

