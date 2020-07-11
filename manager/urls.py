from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^panel/manager/list/$', views.manager_list, name="manager_list"),
    url(r'^panel/manager/delete/(?P<pk>\d+)/$', views.manager_delete, name="manager_delete"),
    
    url(r'^panel/manager/(?P<pk>\d+)/permission/$', views.manager_permission, name="manager_permission"),
    url(r'^panel/manager/(?P<pk>\d+)/permission/(?P<name>.*)/delete/$', views.manager_permission_delete, name="manager_permission_delete"),
    url(r'^panel/manager/(?P<pk>\d+)/permission/add/$', views.manager_permission_add, name="manager_permission_add"),
    
    url(r'^panel/group/$', views.group, name="group"),
    url(r'^panel/group/add/$', views.group_add, name="group_add"),
    url(r'^panel/group/delete/(?P<name>.*)/$', views.group_delete, name="group_delete"),
    url(r'^panel/manager/(?P<pk>\d+)/groups/$', views.manager_in_groups, name="manager_in_groups"),
    url(r'^panel/manager/addgrouptomanager/(?P<pk>\d+)/$', views.add_manager_to_group, name="add_manager_to_group"),
    url(r'^panel/manager/delgroupfrommanager/(?P<name>.*)/(?P<pk>\d+)/$', views.del_group_from_manager, name="del_group_from_manager"),
    
    url(r'^panel/permission/$', views.permission, name="permission"),
    url(r'^panel/permission/delete/(?P<name>.*)/$', views.permission_delete, name="permission_delete"),
    url(r'^panel/permission/add/$', views.permission_add, name="permission_add"),

    url(r'^panel/group/permission/delete/(?P<name>.*)/from/(?P<gname>.*)/$', views.group_permission_delete, name="group_permission_delete"),
    url(r'^panel/group/permission/add/(?P<name>.*)/$', views.group_permission_add, name="group_permission_add"),
    url(r'^panel/group/permission/(?P<name>.*)/$', views.group_permission, name="group_permission"),
 
]