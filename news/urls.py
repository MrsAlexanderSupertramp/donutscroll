from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^panel/news/add/$', views.news_add, name='news_add'),
    url(r'^panel/news/list/$', views.news_list, name='news_list'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
]