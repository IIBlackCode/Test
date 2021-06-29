from django.db import models

class Hospital(models.Model):
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical = models.IntegerField()