from haystack.indexes import *
from haystack import site
from website.models import Page,News,Events,Resource,CaseStudy,Program


class PageIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    content = CharField(model_attr='content')

class NewsIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    long_description = CharField(model_attr='long_description')
    short_description = CharField(model_attr='short_description')
    title = CharField(model_attr='title')

class EventsIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    long_description = CharField(model_attr='long_description')
    short_description = CharField(model_attr='short_description')
    title = CharField(model_attr='title')

class ProgramIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    description = CharField(model_attr='description')
    title = CharField(model_attr='title')

class ResourceIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    long_description = CharField(model_attr='long_description')
    short_description = CharField(model_attr='short_description')
    title = CharField(model_attr='title')

class CaseStudyIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    long_description = CharField(model_attr='long_description')
    short_description = CharField(model_attr='short_description')
    title = CharField(model_attr='title')

site.register(Page, PageIndex)
site.register(News, NewsIndex)
site.register(Events, EventsIndex)
site.register(Program, ProgramIndex)
site.register(Resource, ResourceIndex)
site.register(CaseStudy, CaseStudyIndex)