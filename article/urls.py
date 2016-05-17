from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', article_views.index, name='index'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
]