from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=500000000)
    answer = models.CharField(max_length=50000000000)