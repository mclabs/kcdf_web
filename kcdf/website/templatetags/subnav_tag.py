from django import template
register = template.Library()
from kcdf.website.models import Program,Page


@register.inclusion_tag("website/partials/subnav.html")
def subnav():
	links=[]
	programs=Program.objects.all()
	return {"programs":programs}
	
		
@register.inclusion_tag("website/partials/pages_subnav.html")
def pages_subnav(slug):
	links=[]
	sub_pages=Page.objects.all().exclude(slug=slug)
	return {"sub_pages":sub_pages}
