from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Site


def home(request):
    post = Site.objects.get(alias = 'home')
    template = loader.get_template('main/home.html')
    context = RequestContext(request, {
        'detail':post,
    })
    return HttpResponse(template.render(context))

def site(request, alias):
	post = Site.objects.get(alias = alias);
	template = loader.get_template('main/site.html')
	context = RequestContext(request,{
		'detail':post,
	})
	return HttpResponse(template.render(context))