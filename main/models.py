from __future__ import unicode_literals
from django.db import models

class Main(models.Model):

    name = models.CharField(max_length=50)
    about = models.TextField()
    tw = models.CharField(default="-", max_length=50)
    yt = models.CharField(default="-", max_length=50)
    fb = models.CharField(default="-", max_length=50)
    cell = models.CharField(default="-", max_length=15)

    settings = models.CharField(default="-", max_length=50)

    def __str__(self):
        return self.settings + " | " + str(self.pk)


class Trending(models.Model) :
    name = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.name


class HeadingDropdown(models.Model) :

    catname = models.CharField(max_length=50, default="-")
    name = models.CharField(max_length=100, default="-")
    picurl = models.TextField(default='-')

    def __str__(self):
        return self.name  + " | " + str(self.catname)


class MostViewed(models.Model) :

    catname = models.CharField(max_length=50, default="-")
    name = models.CharField(max_length=100, default="-")
    picurl = models.TextField(default='-')
    date = models.CharField(max_length=50, default="-")

    def __str__(self):
        return self.name  + " | " + str(self.catname)


class FeaturedHome(models.Model) :

    catname = models.CharField(max_length=50, default="-")
    name = models.CharField(max_length=100, default="-")
    picurl = models.TextField(default='-')
    date = models.CharField(max_length=50, default="-")
    position = models.CharField(max_length=50, default="-")
    intro_text = models.TextField() 

    def __str__(self):
        return self.name  + " | " + str(self.catname)


class MasonryHome(models.Model) :
    
    catname = models.CharField(max_length=50, default="-")
    name = models.CharField(max_length=100, default="-")
    picurl = models.TextField(default='-')
    date = models.CharField(max_length=50, default="-")
    position = models.CharField(max_length=50, default="-")
    intro_text = models.TextField() 

    def __str__(self):
        return self.name  + " | " + str(self.catname)


class PicturesGallery(models.Model) :
    givenname = models.CharField(max_length=100, default="-")
    picname = models.CharField(max_length=100, default="-")
    picurl = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.givenname


class ExtraPages(models.Model) :
    pagename = models.CharField(max_length=100, default="-")
    pagecontent = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pagename