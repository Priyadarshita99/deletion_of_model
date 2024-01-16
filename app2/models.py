from django.db import models

# Create your models here.

class Country(models.Model):
    Cname=models.CharField(primary_key=True,max_length=50)
    ccode=models.BigIntegerField()