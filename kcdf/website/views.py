from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import News,Program,ResourceType,Resource,Page
from django.views.generic import list_detail

def index (request):
	news=News.objects.all().order_by("created_at")[:4]
	return render_to_response('website/index.html',{"news":news});
	
def page (request,slug):
	page = get_object_or_404(Page, slug=slug)
	return render_to_response('website/events.html');

def resources (request):
	resources=Resource.objects.all().order_by("created_at")
	context_dict={'active_tab': 'resource-center',"resources":resources}
	return render_to_response('website/resources.html',context_dict);

def case_studies (request):
	news=News.objects.all().order_by("created_at")
	return render_to_response('website/index.html');

def programs(request):
	programs=Program.objects.all()
	context_dict={'active_tab': 'programs',"programs":programs}
	return render_to_response('website/programmes.html',context_dict);

def program_details (request,slug):
	program = get_object_or_404(Program, slug=slug)
	context_dict={'active_tab': 'programs',"program":program}
	return render_to_response('website/program_detail.html',context_dict);