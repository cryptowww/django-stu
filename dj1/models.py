from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    username = models.CharField
    password = models.CharField