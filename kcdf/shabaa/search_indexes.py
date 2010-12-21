from haystack.indexes import *
from haystack import site
from shabaa.models import *

class FunderIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    organisation_name = CharField(model_attr='organisation_name')
    content = CharField(model_attr='mission')

class ServiceProviderIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    organisation_name = CharField(model_attr='organisation_name')
    content = CharField(model_attr='description')
    funding_partners = CharField(model_attr='funding_partners')

class LegalDocumentIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    content = CharField(model_attr='qualification')
    requirements = CharField(model_attr='requirements')

class BusinessRegistrationIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    business_type = CharField(model_attr='business_type')
    requirements = CharField(model_attr='requirements')

class IndividualRegistrationIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    organisation_name = CharField(model_attr='organisation_name')
    description = CharField(model_attr='description')
    requirements = CharField(model_attr='requirements')

class YouthProgramIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    description = CharField(model_attr='description')
    funding_partners = CharField(model_attr='funding_partners')


site.register(Funder, FunderIndex)
site.register(ServiceProvider, ServiceProviderIndex)
site.register(LegalDocument, LegalDocumentIndex)
site.register(BusinessRegistration, BusinessRegistrationIndex)
site.register(IndividualRegistration, IndividualRegistrationIndex)
site.register(YouthProgram, YouthProgramIndex)