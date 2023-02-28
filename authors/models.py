from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

class CustomUser(models.Model):
    username = models.CharField(_('Enter an alias'), max_length=64, unique=True)
    firstname = models.CharField(max_length=64, blank=False)
    lastname = models.CharField(max_length=65, blank=False)
    email = models.EmailField(max_length=65, blank=False, unique=True)