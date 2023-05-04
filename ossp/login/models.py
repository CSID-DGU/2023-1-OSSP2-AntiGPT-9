import datetime
from django.db import models
from django.utils import timezone

class userlogin(models.Model):
    tempemail = models.CharField(max_length=30)
    temppwd = models.CharField(max_length=30)


    