from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import *
from kcdf.shabaa.models import *
from django.views.generic import list_detail
from django.template import RequestContext
from reportlab.pdfgen import canvas
from django.http import HttpResponse



def index (request):
	p=Program.objects.get(slug__contains='youth')
	events=Events.objects.filter(program=p).order_by("-created_at")[:4]
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")[:4]
	news=News.objects.filter(program=p).order_by("-created_at")[:4]
	context_dict={"news":news,"events":events,"cases":cases,"program":p}
	return render_to_response('shabaa/index.html',context_dict,context_instance=RequestContext(request));

def page (request,slug=""):
	program=Program.objects.get(slug__contains='youth')
	page=Page.objects.get(slug__contains='about-youth')
	children=Page.objects.all().filter(parent=page)
	context_dict={'active_tab': 'about-shabaa',"program":program,"children":children}
	return render_to_response('shabaa/page.html',context_dict,context_instance=RequestContext(request));

def inner_page (request,slug=""):
	page = get_object_or_404(Page, slug=slug)
	children=Page.objects.all().filter(parent=page)
	#pages=Page.objects.all().exclude(slug=slug)
	pages=Page.objects.all()
	context_dict={'active_tab': 'about-shabaa',"page":page,"children":children,"pages":pages}
	return render_to_response('shabaa/inner_page.html',context_dict,context_instance=RequestContext(request));



def resources(request):
	p=Program.objects.get(slug__contains='youth')
	resources=Resource.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'resource-center',"resources":resources}
	return render_to_response('shabaa/resources.html',context_dict,context_instance=RequestContext(request));

def resource_detail(request,slug):
	resource = get_object_or_404(Resource, slug=slug)
	context_dict={'active_tab': 'resource',"resource":resource}
	return render_to_response('shabaa/resource_detail.html',context_dict,context_instance=RequestContext(request));


def news(request):
	p=Program.objects.get(slug__contains='youth')
	news=News.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('shabaa/news.html',context_dict,context_instance=RequestContext(request));

def news_detail(request,slug):
	news = get_object_or_404(News, slug=slug)
	context_dict={'active_tab': 'news',"news":news}
	return render_to_response('shabaa/news_detail.html',context_dict,context_instance=RequestContext(request));

def events(request):
	p=Program.objects.get(slug__contains='youth')
	events=Events.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('shabaa/events.html',context_dict,context_instance=RequestContext(request));

def events_detail(request,slug):
	events = get_object_or_404(Events, slug=slug)
	context_dict={'active_tab': 'events',"events":events}
	return render_to_response('shabaa/events_detail.html',context_dict,context_instance=RequestContext(request));


def case_studies (request):
	p=Program.objects.get(slug__contains='youth')
	cases=CaseStudy.objects.filter(program=p).order_by("-created_at")
	context_dict={'active_tab': 'case-studies',"cases":cases}
	return render_to_response('shabaa/casestudies.html',context_dict,context_instance=RequestContext(request));


def casestudy_detail(request,slug):
	casestudy = get_object_or_404(CaseStudy, slug=slug)
	context_dict={'active_tab': 'case-studies',"casestudy":casestudy}
	return render_to_response('shabaa/casestudy_detail.html',context_dict,context_instance=RequestContext(request));


def funders(request):
	funders=Funder.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"funders":funders}
	return render_to_response('shabaa/funders.html',context_dict,context_instance=RequestContext(request));


def funders_detail(request,slug):
	funder = get_object_or_404(Funder, slug=slug)
	context_dict={'active_tab': 'resource-center',"funder":funder}
	return render_to_response('shabaa/funder_detail.html',context_dict,context_instance=RequestContext(request));


def legal_docs(request):
	legal_docs=LegalDocument.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"legal_docs":legal_docs}
	return render_to_response('shabaa/legal_docs.html',context_dict,context_instance=RequestContext(request));

def legal_detail(request,slug):
	legal = get_object_or_404(LegalDocument, slug=slug)
	context_dict={'active_tab': 'resource-center',"legal":legal}
	return render_to_response('shabaa/legal_detail.html',context_dict,context_instance=RequestContext(request));


def indiv_reg(request):
	individual=IndividualRegistration.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"individual":individual}
	return render_to_response('shabaa/individual.html',context_dict,context_instance=RequestContext(request));

def indiv_detail(request,slug):
	individual = get_object_or_404(IndividualRegistration, slug=slug)
	context_dict={'active_tab': 'resource-center',"individual":individual}
	return render_to_response('shabaa/individual_detail.html',context_dict,context_instance=RequestContext(request));


def business_reg(request):
	business=BusinessRegistration.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"business":business}
	return render_to_response('shabaa/business.html',context_dict,context_instance=RequestContext(request));

def business_detail(request,slug):
	business = get_object_or_404(BusinessRegistration, slug=slug)
	context_dict={'active_tab': 'resource-center',"business":business}
	return render_to_response('shabaa/business_detail.html',context_dict,context_instance=RequestContext(request));


def service_prov(request):
	service=ServiceProvider.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"service":service}
	return render_to_response('shabaa/service.html',context_dict,context_instance=RequestContext(request));

def service_detail(request,slug):
	service = get_object_or_404(ServiceProvider, slug=slug)
	context_dict={'active_tab': 'resource-center',"service":service}
	return render_to_response('shabaa/service_detail.html',context_dict,context_instance=RequestContext(request));

def youth_prog(request):
	youth=YouthProgram.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"youth":youth}
	return render_to_response('shabaa/youth.html',context_dict,context_instance=RequestContext(request));

def print_pdf(request,slug):
	from reportlab.lib.units import inch
	
	funder = get_object_or_404(Funder, slug=slug)
	response=HttpResponse(mimetype='application/pdf')
	response['Content-Disposition']='attachment;filename=%s'%(slug)
	c=canvas.Canvas(response)
	text=c.beginText()
	text.setTextOrigin(inch,2.5*inch)
	text.setFont("Helvetica",14)
	text.setFillGray(0,4)
	text.textLine("Organisation name")
	text.textLine(funder.organisation_name)
	text.textLine(funder.eligibility)
	c.drawText(text)
	c.showPage()
	c.save()
	return response