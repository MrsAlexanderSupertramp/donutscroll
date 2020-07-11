from django.contrib import admin
from .models import Comments
from .models import Comments_Reply
from . models import Comments_Doodle

# Register your models here.


admin.site.register(Comments)

admin.site.register(Comments_Reply)

admin.site.register(Comments_Doodle)