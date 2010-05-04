from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from kcdf.website.models import *
from django.views.generic import list_detail
from django.template import RequestContext

def index (request):
	news=News.objects.all().order_by("created_at")[:4]
	return render_to_response('girlchild/index.html',{},context_instance=RequestContext(request));
