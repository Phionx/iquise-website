# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Meeting(models.Model):
    # This will create a file and keep a path to it
    date = models.DateField(default=timezone.now,unique=True)
    attendees = models.ManyToManyField(User,blank=True,limit_choices_to={'is_superuser': False})
    minutes = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s'%self.date
