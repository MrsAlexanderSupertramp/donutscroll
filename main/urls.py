from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^Extended/(?P<cat>.*)/(?P<name>.*)/$', views.news_detail, name="news_detail"),
    url(r'^Category/(?P<name>.*)/$', views.news_section, name="news_section"),
    url(r'^panel/$', views.panel, name="panel"),
    url(r'^login/$', views.mylogin, name="mylogin"),
    url(r'^register/$', views.myregister, name="myregister"),
    url(r'^logout/$', views.mylogout, name="mylogout"),
    url(r'^comment/add/$', views.comments_add, name="comments_add"),
    url(r'^comment/reply/add/$', views.comments_reply_add, name="comments_reply_add"),
    url(r'^search/$', views.news_search, name="news_search"),
    url(r'^trending/forward/(?P<name>.*)/$', views.trending_forward, name="trending_forward"),
    url(r'^error/$', views.error, name="error"),

    url(r'^panel/settings/postbyposition/$', views.post_by_position, name="post_by_position"),
    url(r'^panel/settings/dropdown/add/$', views.heading_dropdown_add, name="heading_dropdown_add"),
    url(r'^panel/settings/dropdown/delete/(?P<pk>\d+)/$', views.heading_dropdown_delete, name="heading_dropdown_delete"),
    url(r'^panel/settings/mostviewed/add/$', views.most_viewed_add, name="most_viewed_add"),
    url(r'^panel/settings/mostviewed/delete/(?P<pk>\d+)/$', views.most_viewed_delete, name="most_viewed_delete"),
    url(r'^panel/settings/featuredhome/add/$', views.featured_home_add, name="featured_home_add"),
    url(r'^panel/settings/featuredhome/delete/(?P<pk>\d+)/$', views.featured_home_delete, name="featured_home_delete"),
    url(r'^panel/settings/masonryhome/add/$', views.masonry_home_add, name="masonry_home_add"),
    url(r'^panel/settings/masonryhome/delete/(?P<pk>\d+)/$', views.masonry_home_delete, name="masonry_home_delete"),
    url(r'^panel/settings/pictures/$', views.pictures_gallery, name="pictures_gallery"),
    url(r'^panel/settings/pictures/add/$', views.pictures_gallery_add, name="pictures_gallery_add"),
    url(r'^panel/settings/pictures/delete/(?P<pk>\d+)$', views.pictures_gallery_delete, name="pictures_gallery_delete"),
    url(r'^panel/settings/extrapages/$', views.extra_pages, name="extra_pages"),
    url(r'^panel/settings/extrapages/add/$', views.extra_pages_add, name="extra_pages_add"),
    url(r'^panel/settings/extrapages/delete/(?P<pk>\d+)/$', views.extra_pages_delete, name="extra_pages_delete"),
    url(r'^panel/settings/extrapages/content/(?P<pk>\d+)/$', views.extra_pages_content, name="extra_pages_content"),
    url(r'^panel/settings/trending/list/$', views.trending_list, name='trending_list'),
    url(r'^panel/settings/trending/remove/(?P<pk>\d+)$', views.trending_remove, name='trending_remove'),

    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^copyright-policy/$', views.copyright, name="copyright"),
    url(r'^cookie-policy/$', views.cookie_policy, name="cookie_policy"),
    url(r'^ethics-policy/$', views.ethics_policy, name="ethics_policy"),
    url(r'^ownership-policy/$', views.ownership, name="ownership"),
    url(r'^privacy-policy/$', views.privacy_policy, name="privacy_policy"),
    url(r'^terms-of-service/$', views.terms_of_service, name="terms_of_service"),
    url(r'^diversity-and-corrections-policy/$', views.diversity_and_corrections_policy, name="diversity_and_corrections_policy"),



]