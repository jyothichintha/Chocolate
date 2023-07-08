from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chocolate(models.Model):

    cname = models.CharField(max_length = 150,primary_key = True)
    flavour=models.CharField(max_length=100)
    cimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    cost = models.IntegerField()
    description = models.TextField(default ='chocolate')
    def __str__(self):
        return self.cname
        