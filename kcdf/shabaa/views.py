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
	all_funders=Funder.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"funder":funder,"all_funders":all_funders}
	return render_to_response('shabaa/funder_detail.html',context_dict,context_instance=RequestContext(request));


def legal_docs(request):
	legal_docs=LegalDocument.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"legal_docs":legal_docs}
	return render_to_response('shabaa/legal_docs.html',context_dict,context_instance=RequestContext(request));

def legal_detail(request,slug):
	legal = get_object_or_404(LegalDocument, slug=slug)
	all_legal=LegalDocument.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"legal":legal,"all_legal":all_legal}
	return render_to_response('shabaa/legal_detail.html',context_dict,context_instance=RequestContext(request));


def indiv_reg(request):
	individual=IndividualRegistration.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"individual":individual}
	return render_to_response('shabaa/individual.html',context_dict,context_instance=RequestContext(request));

def indiv_detail(request,slug):
	individual = get_object_or_404(IndividualRegistration, slug=slug)
	all_indiv=IndividualRegistration.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"individual":individual,"all_indiv":all_indiv}
	return render_to_response('shabaa/individual_detail.html',context_dict,context_instance=RequestContext(request));


def business_reg(request):
	business=BusinessRegistration.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"business":business}
	return render_to_response('shabaa/business.html',context_dict,context_instance=RequestContext(request));

def business_detail(request,slug):
	business = get_object_or_404(BusinessRegistration, slug=slug)
	all_business=BusinessRegistration.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"business":business,"all_business":all_business}
	return render_to_response('shabaa/business_detail.html',context_dict,context_instance=RequestContext(request));


def service_prov(request):
	service=ServiceProvider.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"service":service}
	return render_to_response('shabaa/service.html',context_dict,context_instance=RequestContext(request));

def service_detail(request,slug):
	service = get_object_or_404(ServiceProvider, slug=slug)
	all_service=ServiceProvider.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"service":service,"all_service":all_service}
	return render_to_response('shabaa/service_detail.html',context_dict,context_instance=RequestContext(request));

def youth_prog(request):
	youth=YouthProgram.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"youth":youth}
	return render_to_response('shabaa/youth.html',context_dict,context_instance=RequestContext(request));

def youth_detail(request,slug):
	youth = get_object_or_404(YouthProgram, slug=slug)
	all_youth=YouthProgram.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"youth":youth,"all_youth":all_youth}
	return render_to_response('shabaa/youth_detail.html',context_dict,context_instance=RequestContext(request));

def parks(request):
	park=NationalPark.objects.all().order_by("-id")
	context_dict={'active_tab': 'resource-center',"park":park}
	return render_to_response('shabaa/parks.html',context_dict,context_instance=RequestContext(request));

def park(request,slug):
	park = get_object_or_404(NationalPark, slug=slug)
	all_parks=NationalPark.objects.exclude(slug=slug).order_by("-id")[:5]
	context_dict={'active_tab': 'resource-center',"park":park,"all_parks":all_parks}
	return render_to_response('shabaa/park_detail.html',context_dict,context_instance=RequestContext(request));


def print_pdf(request,slug):
	from reportlab.lib.units import inch
	from django.utils.html import strip_tags
	from reportlab.pdfbase.pdfmetrics import stringWidth
	from reportlab.rl_config import defaultPageSize

	PAGE_WIDTH  = defaultPageSize[0]
	PAGE_HEIGHT = defaultPageSize[1]

	
	funder = get_object_or_404(Funder, slug=slug)
	response=HttpResponse(mimetype='application/pdf')
	response['Content-Disposition']='attachment;filename=%s'%(slug)
	c=canvas.Canvas(response)
	sample_text=strip_tags(funder.eligibility)
	text_width = stringWidth(sample_text,"Helvetica",14)
	y = 1050
	text=c.beginText((PAGE_WIDTH - text_width) / 2.0, y)
	text.setTextOrigin(inch,2.5*inch)
	text.setFont("Helvetica",14)
	text.textLine("Organisation name")
	text.textLine(funder.organisation_name)
	text.textLines(strip_tags(funder.eligibility))
	c.drawText(text)
	c.showPage()
	c.save()
	return response

def map(request):
	grantees=Grantee.objects.filter(start_year=sYear,end_year=eYear)
	template = "shabaa/grantees_map.json"
	context_dict={'active_tab': 'grantees',"grantees":grantees}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));
	
def grantees_by_year (request,sYear="",eYear=""):
	p=Program.objects.get(slug__contains='youth')
	grantees=Grantee.objects.filter(start_year=sYear,end_year=eYear,program=p)
	template = "shabaa/grantees_by_year.html"
	context_dict={'active_tab': 'grantees',"grantees":grantees}
	return render_to_response(template,context_dict,context_instance=RequestContext(request));
