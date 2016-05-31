# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import markdown

# Create your views here.
def index(request):
    post_list = Article.objects.all()
    return render(request, 'index.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        post.content = markdown.markdown(post.content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite'])
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})

def about_me(request) :
    return render(request, 'aboutme.html')

def google(request) :
    return render(request, 'googledcbd985fda3b59cb.html')

def baidu(request) :
    return render(request, 'baidu_verify_MvQnvdgfUB.html')

def listing(request):
    contact_list = Article.objects.all()
    paginator = Paginator(contact_list, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'contacts': contacts})

