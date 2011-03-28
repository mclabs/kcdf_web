from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import *
from django.views.generic import list_detail
from django.template import RequestContext

def index (request):
	p=Program.objects.get(slug__contains='food-security')
	news=News.objects.filter(program=p).order_by("-created_at")[:4]
	events=Events.objects.filter(program=p).order_by("-created_at")[:4]
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")
	context_dict={"news":news,"events":events,"cases":cases,"program":p}
	return render_to_response('ustawi/index.html',context_dict,context_instance=RequestContext(request));

def page (request,slug=""):
	program=Program.objects.get(slug__contains='food-security')
	page=Page.objects.get(slug__contains='about-ustawi')
	children=Page.objects.all().filter(parent=page)
	context_dict={'active_tab': 'about-ustawi',"program":program,"children":children}
	return render_to_response('ustawi/page.html',context_dict,context_instance=RequestContext(request));

def inner_page (request,slug=""):
	page = get_object_or_404(Page, slug=slug)
	children=Page.objects.all().filter(parent=page)
	#pages=Page.objects.all().exclude(slug=slug)
	pages=Page.objects.all()
	context_dict={'active_tab': 'about-ustawi',"page":page,"children":children,"pages":pages}
	return render_to_response('ustawi/inner_page.html',context_dict,context_instance=RequestContext(request));


def resources(request):
	p=Program.objects.get(slug__contains='food-security')
	resources=Resource.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'resource-center',"resources":resources}
	return render_to_response('ustawi/resources.html',context_dict,context_instance=RequestContext(request));

def resource_detail(request,slug):
	resource = get_object_or_404(Resource, slug=slug)
	context_dict={'active_tab': 'resource',"resource":resource}
	return render_to_response('ustawi/resource_detail.html',context_dict,context_instance=RequestContext(request));


def news(request):
	p=Program.objects.get(slug__contains='food-security')
	news=News.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('ustawi/news.html',context_dict,context_instance=RequestContext(request));

def news_detail(request,slug):
	news = get_object_or_404(News, slug=slug)
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('ustawi/news_detail.html',context_dict,context_instance=RequestContext(request));


def events(request):
	p=Program.objects.get(slug__contains='food-security')
	events=Events.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('ustawi/events.html',context_dict,context_instance=RequestContext(request));

def events_detail(request,slug):
	events = get_object_or_404(Events, slug=slug)
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('ustawi/events_detail.html',context_dict,context_instance=RequestContext(request));


def case_studies (request):
	p=Program.objects.get(slug__contains='food-security')
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'case-studies',"cases":cases}
	return render_to_response('ustawi/casestudies.html',context_dict,context_instance=RequestContext(request));


def casestudy_detail(request,slug):
	casestudy = get_object_or_404(CaseStudy, slug=slug)
	context_dict={'active_tab': 'case-studies',"casestudy":casestudy}
	return render_to_response('ustawi/casestudy_detail.html',context_dict,context_instance=RequestContext(request));

def grantees_by_year (request,sYear="",eYear=""):
	p=Program.objects.get(slug__contains='food-security')
	grantees=Grantee.objects.filter(start_year=sYear,end_year=eYear,program=p)
	template = "ustawi/grantees_by_year.html"
	context_dict={'active_tab': 'grantees',"grantees":grantees}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

def videos(request):
	p=Program.objects.get(slug__contains='food-security')
	videos=Video.objects.filter(status__exact='1').order_by("-id")
	context_dict={'active_tab': 'resource-center',"videos":videos}
	return render_to_response('ustawi/videos.html',context_dict,context_instance=RequestContext(request));

def video_details (request,slug):
	video = get_object_or_404(Video, slug=slug)
	template = "ustawi/video_detail.html"
	context_dict={'active_tab': 'resource-center',"video":video}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));


def audios(request):
	p=Program.objects.get(slug__contains='food-security')
	audios=Audio.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"audios":audios}
	return render_to_response('ustawi/audios.html',context_dict,context_instance=RequestContext(request));

def audio_details (request,slug):
	audio = get_object_or_404(Audio, slug=slug)
	template = "ustawi/audio_detail.html"
	context_dict={'active_tab': 'resource-center',"audio":audio}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

def downloads(request):
	p=Program.objects.get(slug__contains='food-security')
	downloads=Downloads.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource',"downloads":downloads}
	return render_to_response('ustawi/downloads.html',context_dict,context_instance=RequestContext(request));

def download_details (request,slug):
	download = get_object_or_404(Downloads, slug=slug)
	template = "ustawi/download_detail.html"
	context_dict={'active_tab': 'resource-center',"download":download}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));
