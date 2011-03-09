from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import *
from django.views.generic import list_detail
from django.template import RequestContext

def index (request):
	p=Program.objects.get(slug__contains='arts')
	news=News.objects.filter(program=p).order_by("-created_at")[:4]
	events=Events.objects.filter(program=p).order_by("-created_at")[:4]
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")[:4]
	context_dict={"news":news,"events":events,"cases":cases,"program":p}
	return render_to_response('arts/index.html',context_dict,context_instance=RequestContext(request));

def page (request,slug=""):
	program=Program.objects.get(slug__contains='arts')
	page=Page.objects.get(slug__contains='about-arts')
	children=Page.objects.all().filter(parent=page)
	context_dict={'active_tab': 'about-arts',"program":program,"children":children}
	return render_to_response('arts/page.html',context_dict,context_instance=RequestContext(request));


def inner_page (request,slug=""):
	page = get_object_or_404(Page, slug=slug)
	children=Page.objects.all().filter(parent=page)
	#pages=Page.objects.all().exclude(slug=slug)
	pages=Page.objects.all()
	context_dict={'active_tab': 'about-arts',"page":page,"children":children,"pages":pages}
	return render_to_response('arts/inner_page.html',context_dict,context_instance=RequestContext(request));



def resources(request):
	p=Program.objects.get(slug__contains='arts')
	resources=Resource.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'resource-center',"resources":resources}
	return render_to_response('arts/resources.html',context_dict,context_instance=RequestContext(request));

def resource_detail(request,slug):
	p=Program.objects.get(slug__contains='arts')
	resources=Resource.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'resource',"resource":resources}
	return render_to_response('arts/resource_detail.html',context_dict,context_instance=RequestContext(request));


def news(request):
	p=Program.objects.get(slug__contains='arts')
	news=News.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('arts/news.html',context_dict,context_instance=RequestContext(request));

def news_detail(request,slug):
	news = get_object_or_404(News, slug=slug)
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('arts/news_detail.html',context_dict,context_instance=RequestContext(request));

def events(request):
	p=Program.objects.get(slug__contains='arts')
	events=Events.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('arts/events.html',context_dict,context_instance=RequestContext(request));

def events_detail(request,slug):
	events = get_object_or_404(Events, slug=slug)
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('arts/events_detail.html',context_dict,context_instance=RequestContext(request));


def case_studies (request):
	p=Program.objects.get(slug__contains='arts')
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'case-studies',"cases":cases}
	return render_to_response('arts/casestudies.html',context_dict,context_instance=RequestContext(request));


def casestudy_detail(request,slug):
	casestudy = get_object_or_404(CaseStudy, slug=slug)
	context_dict={'active_tab': 'case-studies',"casestudy":casestudy}
	return render_to_response('arts/casestudy_detail.html',context_dict,context_instance=RequestContext(request));

def grantees_by_year (request,sYear="",eYear=""):
	p=Program.objects.get(slug__contains='arts')
	grantees=Grantee.objects.filter(start_year=sYear,end_year=eYear,program=p)
	template = "arts/grantees_by_year.html"
	context_dict={'active_tab': 'grantees',"grantees":grantees}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));

