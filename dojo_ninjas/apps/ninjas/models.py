from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(text_field=300)

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

