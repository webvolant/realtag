from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#import os
from models import Post
from models import Category
from models import Tag

from django.conf import settings #import variables from settings


from django.contrib import auth

class WCategory(object):
    wid = 0
    wcount = 0
    wname = "wname"
    def __init__(self, wid, wcount, wname):    
        self.wid = wid
        self.wcount = wcount
        self.wname = wname
    def __setitem__(self, key, item): 
        self.key = item

def getCat():
    category = Category.objects.filter(status=settings.STATUS_SHOW)
    kolcat = len(category)

    #wlist = [ WCategory(i,0,"x") for i in range(10)]
    my_objects = []
    i=1
    for i in range(kolcat+1):
        my_objects.append(WCategory(i,0,"empty"))

    i=1
    for c in category:
        my_objects[i].wcount = len(Post.objects.filter(category = c.id))
        my_objects[i].wname = c.name
        my_objects[i].wid = c.id
        i=i+1
    del my_objects[0]
    return my_objects

def getPaginate(request,list,var):
    paginator = Paginator(list, var) # Show 8 contacts per page

    page = request.GET.get('page')
    try:
        list_of_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_of_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_of_objects = paginator.page(paginator.num_pages)
    return list_of_objects

def index(request):
    post_list_limit = Post.objects.filter(category__status=settings.STATUS_SHOW,status=settings.STATUS_SHOW).order_by('-ddate')[:settings.ARTICLES_COUNT] # for module
    my_objects = getCat() #for module category with count

    post_list = Post.objects.filter(category__status=settings.STATUS_SHOW,status=settings.STATUS_SHOW).order_by('-ddate')
    list_of_objects = getPaginate(request,post_list,settings.ARTICLES_COUNT_PAGE)

    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_post_list': list_of_objects,
        'post_list_limit': post_list_limit,
        'objwcat':my_objects,
    })
    return HttpResponse(template.render(context))

def category(request, catid):
    post_list_limit = Post.objects.filter(category__status=settings.STATUS_SHOW,status=settings.STATUS_SHOW).order_by('-ddate')[:settings.ARTICLES_COUNT] # for module
    my_objects = getCat() #for module category with count

    post_list = Post.objects.filter(category = catid,category__status=settings.STATUS_SHOW,status=settings.STATUS_SHOW).order_by('-ddate') #? status &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    list_of_objects = getPaginate(request,post_list,settings.ARTICLES_COUNT_PAGE)

    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_post_list': list_of_objects,
        'post_list_limit': post_list_limit,
        'objwcat':my_objects,
    })
    return HttpResponse(template.render(context))

def detail(request, post_id): #detail ,in article
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access/')
    else:
        post_list_limit = Post.objects.filter(category__status=settings.STATUS_SHOW,status=settings.STATUS_SHOW).order_by('-ddate')[:settings.ARTICLES_COUNT] # for module
        my_objects = getCat() #for module category with count

        post = Post.objects.get(id = post_id,status=settings.STATUS_SHOW)

        tags = Tag.objects.filter(post = post_id)

        template = loader.get_template('blog/detail.html')
        context = RequestContext(request, {
            'latest_post': post,
            'post_list_limit': post_list_limit,
            'objwcat':my_objects,
            'tags':tags,
        })
        return HttpResponse(template.render(context))


  