from django.contrib.auth import forms
from django.contrib.auth.models import User

from django.db import models



class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name
