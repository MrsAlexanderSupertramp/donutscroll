from __future__ import unicode_literals
from django.db import models


class Comments(models.Model) :

    body    = models.TextField(default="-", null=True, blank=True)
    name    = models.CharField(max_length=50, default="-", null=True, blank=True)
    email   = models.CharField(max_length=50, default="-", null=True, blank=True)
    date    = models.CharField(max_length=40, default="-")
    news_id = models.IntegerField(default=0)
    count   = models.IntegerField(default=0)
    picurl  = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.body


class Comments_Reply(models.Model) :

    body  = models.TextField(default="-", null=True, blank=True)
    name  = models.CharField(max_length=50, default="-", null=True, blank=True)
    email  = models.CharField(max_length=50, default="-", null=True, blank=True)
    date    = models.CharField(max_length=40, default="-")
    news_id = models.IntegerField(default=0)
    comment_id = models.IntegerField(default=0)
    picurl  = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.body


class Comments_Doodle(models.Model) :

    comments_custom_picname = models.CharField(max_length=50, default="-")
    comments_picurl = models.TextField(default="-")
    comments_picname = models.TextField(default="-")

    def __str__(self):
        return self.comments_custom_picname
