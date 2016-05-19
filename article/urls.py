from django.conf.urls import url

from . import views

from article import views as article_views

urlpatterns = [
    url(r'^$', article_views.index, name='index'),
    url(r'^(?P<category>\S+)/(?P<id>\d+)/$', article_views.detail, name='detail'),
]