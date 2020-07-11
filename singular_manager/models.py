from django.db import models


class Singular_Manager(models.Model):

    identifier_home = models.CharField(max_length=50)
