from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^newsletter/add/$', views.news_letter, name="news_letter"),
    url(r'^panel/newsletter/list/$', views.news_letter_list, name="news_letter_list"),
    url(r'^panel/newsletter/delete/(?P<pk>\d+)/$', views.news_letter_delete, name="news_letter_delete"),

]