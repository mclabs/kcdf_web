from django import template
from django.template import loader, Node, Variable
from django.utils.encoding import smart_str, smart_unicode
from django.template.defaulttags import url
from django.template import VariableDoesNotExist
import datetime

register = template.Library()
@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

register = template.Library()
def feedparsed(value):
	return datetime.datetime(*value[:6])
register.filter(feedparsed)
	