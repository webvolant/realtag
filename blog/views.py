from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os

from models import Post

def index(request):
    post_list = Post.objects.order_by('-ddate')
    paginator = Paginator(post_list, 7) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        list_of_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_of_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_of_objects = paginator.page(paginator.num_pages)



    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_post_list': list_of_objects,
    })
    return HttpResponse(template.render(context))

def detailblog(request, post_id):
	latest_post = Post.objects.get(id = post_id);
	template = loader.get_template('blog/detail.html')
	context = RequestContext(request, {
    	'latest_post': latest_post,
    })
	return HttpResponse(template.render(context))


    #try:
    #p = Publisher.objects.get(name='Apress')
#except Publisher.DoesNotExist:
#    print "Apress isn't in the database yet."
#else:
#    print "Apress is in the database."