from django.db import models

# Create your models here.
class contect(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    Content=models.CharField(max_length=400)
    number=models.CharField(max_length=13)