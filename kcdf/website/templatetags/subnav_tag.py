from django import template
register = template.Library()
from kcdf.website.models import Program


@register.inclusion_tag("website/partials/subnav.html")
def subnav():
	links=[]
	programs=Program.objects.all()
	return {"programs":programs}
	
		
