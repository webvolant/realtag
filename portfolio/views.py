# ~*~ coding: utf-8 ~*~
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import os
import socket

from models import Job
from models import Category

def index(request):
    category = Category.objects.all()
    latest_post_list = Job.objects.order_by('-name')
    #output = ', '.join([p.name for p in latest_post_list])
    #return HttpResponse(output)
    #oss = os.path.dirname(os.path.dirname(__file__))
    template = loader.get_template('portfolio/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'socket': socket.gethostname(),
        'category':category,
    })
    return HttpResponse(template.render(context))

def category(request, catid):
    category = Category.objects.all()
    latest_post_list = Job.objects.filter(category=catid)
    
    template = loader.get_template('portfolio/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'category':category,
    })
    return HttpResponse(template.render(context))

def detail(request, post_id):
	latest_post = Job.objects.get(id = post_id);
	template = loader.get_template('portfolio/detail.html')
	context = RequestContext(request, {
    	'latest_post': latest_post,
    })
	return HttpResponse(template.render(context))