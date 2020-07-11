from __future__ import unicode_literals
from django.db import models

class Newsletter(models.Model) :

    email = models.CharField(max_length=50, default="-")
    name = models.CharField(max_length=50, default="-")



    def __str__(self) :
        return self.name + " | " + self.email