from django.contrib import admin
from shabaa.models import *

class ServiceProviderAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','organisation_name')


class LegalDocumentAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','title')

class FunderAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','organisation_name')



admin.site.register(OrganisationCategory)
admin.site.register(OrganisationType)
admin.site.register(ServiceType)
admin.site.register(ServiceProvider,ServiceProviderAdmin)
admin.site.register(LegalDocument,LegalDocumentAdmin)
admin.site.register(Funder,FunderAdmin)

