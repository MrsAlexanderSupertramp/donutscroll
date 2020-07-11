from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views
from news import views

urlpatterns = [
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'', include('news.urls')),
    url(r'', include('category.urls')),
    url(r'', include('singular_manager.urls')),
    url(r'', include('comments.urls')),
    url(r'', include('manager.urls')),
    url(r'', include('newsletter.urls')),
]

urlpatterns += static(
    settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



