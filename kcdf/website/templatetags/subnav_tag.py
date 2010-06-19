from django import template
register = template.Library()
from kcdf.website.models import *


@register.inclusion_tag("website/partials/subnav.html")
def subnav():
	links=[]
	programs=Program.objects.all()
	return {"programs":programs}
	
		
@register.inclusion_tag("website/partials/pages_subnav.html")
def pages_subnav(slug):
	links=[]
	#sub_pages=Page.objects.all().exclude(slug=slug)
	page = Page.objects.all().filter(slug=slug)
	sub_pages=Page.objects.all().filter(parent=page)
	return {"sub_pages":sub_pages}


@register.inclusion_tag("website/partials/slideshow.html")
def slideshow():
	links=[]
	headlines=Headline.objects.all().filter(status=1).order_by("-id")[:5]
	return {"headlines":headlines}

@register.inclusion_tag("website/partials/stats.html")
def stats():
	stats=Stats.objects.all().order_by("-id")[:1]
	return {"stats":stats}
