from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import *
from kcdf.shabaa.models import *
from django.views.generic import list_detail
from django.template import RequestContext

def index (request):
	news=News.objects.all().order_by("-created_at")[:4]
	downloads=Downloads.objects.all().order_by("-id")[:4]
	shabaa=ProjectPartner.objects.all().order_by("-id")
	stats=Stats.objects.all().order_by("-id")[:1]
	context_dict={"news":news,"downloads":downloads,"stats":stats,"shabaa":shabaa}
	return render_to_response('website/index.html',context_dict,context_instance=RequestContext(request));
	
def downloads(request):
	downloads=Downloads.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource',"downloads":downloads}
	return render_to_response('website/downloads.html',context_dict,context_instance=RequestContext(request));
	
def page (request,slug):
	page = get_object_or_404(Page, slug=slug)
	children=Page.objects.all().filter(parent=page)
	#pages=Page.objects.all().exclude(slug=slug)
	pages=Page.objects.all()
	context_dict={'active_tab': 'page',"page":page,"children":children,"pages":pages}
	return render_to_response('website/page.html',context_dict,context_instance=RequestContext(request));

	

def resources(request):
	resources=Resource.objects.all().order_by("-created_at")
	context_dict={'active_tab': 'resource-center',"resources":resources}
	return render_to_response('website/resources.html',context_dict,context_instance=RequestContext(request));

def resource_detail(request,slug):
	resource = get_object_or_404(Resource, slug=slug)
	context_dict={'active_tab': 'resource-center',"resource":resource}
	return render_to_response('website/resource_detail.html',context_dict,context_instance=RequestContext(request));


def news(request):
	news=News.objects.all().order_by("-created_at")
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('website/news.html',context_dict,context_instance=RequestContext(request));

def news_detail(request,slug):
	news = get_object_or_404(News, slug=slug)
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('website/news_detail.html',context_dict,context_instance=RequestContext(request));

def events(request):
	events=Events.objects.all().order_by("-created_at")
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('website/events.html',context_dict,context_instance=RequestContext(request));

def events_detail(request,slug):
	events = get_object_or_404(Events, slug=slug)
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('website/events_detail.html',context_dict,context_instance=RequestContext(request));



def case_studies (request):
	cases=CaseStudy.objects.all().order_by("-created_at")
	context_dict={'active_tab': 'resource',"cases":cases}
	return render_to_response('website/casestudies.html',context_dict,context_instance=RequestContext(request));

def casestudy_detail(request,slug):
	casestudy = get_object_or_404(CaseStudy, slug=slug)
	context_dict={'active_tab': 'resource',"casestudy":casestudy}
	return render_to_response('website/casestudy_detail.html',context_dict,context_instance=RequestContext(request));


def programs(request):
	programs=Program.objects.all()
	context_dict={'active_tab': 'programs',"programs":programs}
	return render_to_response('website/programmes.html',context_dict,context_instance=RequestContext(request));

def program_details (request,slug):
	program = get_object_or_404(Program, slug=slug)
	template = "website/program_detail.html"
	context_dict={'active_tab': 'programs',"program":program}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

def videos(request):
	videos=Video.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"events":videos}
	return render_to_response('website/videos.html',context_dict,context_instance=RequestContext(request));

def video_details (request,slug):
	video = get_object_or_404(Video, slug=slug)
	template = "website/video_detail.html"
	context_dict={'active_tab': 'resource-center',"video":video}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

def download_details (request,slug):
	download = get_object_or_404(Downloads, slug=slug)
	template = "website/download_detail.html"
	context_dict={'active_tab': 'resource-center',"download":download}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

def grantees_by_year (request,sYear="",eYear=""):
	grantees=Grantee.objects.filter(start_year=sYear,end_year=eYear)
	template = "website/grantees_by_year.html"
	context_dict={'active_tab': 'grantees',"grantees":grantees}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));
	

def rapid(request):
	html="message received"	
	return HttpResponse(html)