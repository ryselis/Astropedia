# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import models as auth_models

# Create your models here.
class ScientistsAsks(models.Model):
    date = models.DateTimeField(u'Prašymo data', auto_now_add=True)
    status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True)
    user = models.ForeignKey('User', verbose_name=u'Vartotojas')

class User(auth_models.User):
	is_banned =  models.BooleanField(u'Ar uždraustas', default=False)

class UserSubmittedInfo(models.Model):
	odjecktId = IntegerField(u'Objekto Numeris')
	status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True)
	date = models.DateTimeField(u'Prašymo data',auto_now_add=True)
	user = models.ForeignKey('User', verbose_name=u'Vartotojas')
