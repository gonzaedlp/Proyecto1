from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.
class FamilyApp(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    creation_date=models.DateField(auto_now_add=True,null=True, blank=True)

