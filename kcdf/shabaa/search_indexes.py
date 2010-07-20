from haystack.indexes import *
from haystack import site
from shabaa.models import *

class FunderIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    organisation_name = CharField(model_attr='organisation_name')
    content = CharField(model_attr='mission')

site.register(Funder, FunderIndex)