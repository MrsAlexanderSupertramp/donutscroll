from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^panel/comments/list/$', views.comments_list, name="comments_list"),
    url(r'^panel/comments/delete/(?P<pk>\d+)/$', views.comments_delete, name="comments_delete"),
    url(r'^panel/comments/doodle/add/$', views.doodle_add, name="doodle_add"),
    url(r'^panel/comments/doodle/list/$', views.doodle_list, name="doodle_list"),
    url(r'^panel/comments/doodle/delete/(?P<pk>\d+)/$', views.doodle_delete, name="doodle_delete"),
    url(r'^panel/comments/reply/(?P<pk>\d+)/delete/(?P<news_pk>\d+)/$', views.comments_reply_delete, name="comments_reply_delete"),
    url(r'^panel/comments/(?P<pk>\d+)/reply/list/$', views.comments_reply_list, name="comments_reply_list"),
    



]