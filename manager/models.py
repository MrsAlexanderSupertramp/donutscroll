from __future__ import unicode_literals
from django.db import models



class Manager(models.Model) :
    
    name = models.CharField(max_length=30)
    username = models.TextField()
    email = models.CharField(max_length=30, default="")

    def __str__(self) :
        return self.name
