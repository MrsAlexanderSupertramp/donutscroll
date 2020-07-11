from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^panel/singular_manager/trending/list/$', views.trending_list, name='trending_list'),
    url(r'^panel/singular_manager/trending/remove/(?P<pk>\d+)$', views.trending_remove, name='trending_remove'),

    url(r'^panel/singular_manager/identifier_home/list/$', views.identifier_home_list, name='identifier_home_list'),
    url(r'^panel/singular_manager/identifier_home/add/$', views.identifier_home_add, name='identifier_home_add'),
    url(r'^panel/singular_manager/identifier_home/edit/(?P<pk>\d+)$', views.identifier_home_edit, name='identifier_home_edit'),
    url(r'^panel/singular_manager/identifier_home/remove/(?P<pk>\d+)$', views.identifier_home_remove, name='identifier_home_remove'),
]