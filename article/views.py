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
# def index(request):
#     post_list = Article.objects.all()
#     return render(request, 'index.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
<<<<<<< HEAD
        post.content = markdown.markdown(post.content, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])
        '''
        last_view = request.session.get('last_view')#获取最后一次浏览本站的时间last_view
        if last_view:
            last_visit_time = datetime.datetime.strptime(last_view[:-7], "%Y-%m-%d %H:%M:%S")
        if datetime.datetime.now() >= last_visit_time + datetime.timedelta(minutes=5):#判断如果最后一次访问网站的时间大于5分钟，则浏览量+1
            post.views += 1
            post.save()
        else:
            post.views += 1
            post.save()
        request.session['last_view'] = str(datetime.datetime.now())#更新session
	'''
=======
        post.content = markdown.markdown(post.content,
                                         extensions=['markdown.extensions.extra',
                                                     'markdown.extensions.codehilite'])
>>>>>>> 039a35a9ce35b38bab317f04df786c954f82936e
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

def notfound(request) :
    return render(request, '404.html')

def index(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 5) #每页显示五个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'index.html', {'post_list': post_list})


