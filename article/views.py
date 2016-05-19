# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
import markdown

# Create your views here.
def index(request):
    post_list = Article.objects.all()
    return render(request, 'index.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        cate = Article.objects.get(post.categroy)
        post.content = markdown.markdown(post.content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite'])
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'categroy/post.html', {'categroy': cate, 'post': post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})