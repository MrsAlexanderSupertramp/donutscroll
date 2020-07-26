from django.contrib import admin
from .models import Main, Trending, HeadingDropdown,MostViewed, FeaturedHome, MasonryHome,PicturesGallery,ExtraPages
from django.contrib.auth.models import Permission

admin.site.register(Main)
admin.site.register(Permission)
admin.site.register(Trending)
admin.site.register(HeadingDropdown)
admin.site.register(MostViewed)
admin.site.register(FeaturedHome)
admin.site.register(MasonryHome)
admin.site.register(PicturesGallery)
admin.site.register(ExtraPages)