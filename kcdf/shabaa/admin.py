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

class IndividualRegistrationAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','organisation_name')

class BusinessRegistrationAdmin(admin.ModelAdmin):
	exclude=('slug',)
	list_display = ('id','business_types')


admin.site.register(OrganisationCategory)
admin.site.register(OrganisationType)
admin.site.register(ServiceType)
admin.site.register(ServiceProvider,ServiceProviderAdmin)
admin.site.register(LegalDocument,LegalDocumentAdmin)
admin.site.register(Funder,FunderAdmin)
admin.site.register(BusinessRegistration,BusinessRegistrationAdmin)
admin.site.register(IndividualRegistration,IndividualRegistrationAdmin)

