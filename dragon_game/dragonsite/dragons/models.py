# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dragon(models.Model):
	name = models.CharField(max_length=200)
	tail = models.CharField(max_length=200)
	birth_date = models.DateTimeField('date published')
	
class Choice(models.Model):
    question = models.ForeignKey(Dragon, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)