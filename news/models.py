from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):

    name = models.CharField(max_length=100, default="-")
    intro_text = models.TextField() 
    body_text = RichTextUploadingField() 
    date = models.CharField(max_length=12, default="-")
    time = models.CharField(max_length=12, default="00:00")
    picurl = models.TextField(default='-')
    picname = models.TextField(default="-")
    writer = models.CharField(max_length=50, default="-")
    catname = models.CharField(max_length=50, default="-")
    catid = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    trending = models.BooleanField(default=False)
    identifier_home = models.CharField(max_length=25, default="-")

    def __str__(self):
        return self.name