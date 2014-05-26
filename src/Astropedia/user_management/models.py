# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import models as auth_models

# Create your models here.


class ScientistsAsks(models.Model):
    STATE_UNCONFIRMED = '0'
    STATE_CONFIRMED = '1'
    STATE_REJECTED = '2'
    STATUS_CHOICES = ((STATE_UNCONFIRMED, u'Nepatvirtintas'),
                      (STATE_CONFIRMED, u'Patvirtintas'),
                      (STATE_REJECTED, u'Atmestas'))
    date = models.DateTimeField(u'Prašymo data', auto_now_add=True)
    status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True, choices=STATUS_CHOICES)
    user = models.ForeignKey(auth_models.User, verbose_name=u'Vartotojas')
    class Meta:
        verbose_name = u'Prašymas tapti mokslininku'
        verbose_name_plural = u'Prašymai tapti mokslininku'

class User(auth_models.User):
    is_banned = models.BooleanField(u'Ar uždraustas', default=False)
    class Meta:
        verbose_name = u'Vartotojas'
        verbose_name_plural = u'Vartotojai'


class UserSubmittedInfo(models.Model):
    STATUS_PENDING = '0'
    STATUS_ACCEPTED = '1'
    STATUS_CHOICES = ((STATUS_PENDING, u'Laukia patvirtinimo'),
                      (STATUS_ACCEPTED, u'Patvirtintas'))
    odjecktId = IntegerField(u'Objekto Numeris')
    status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True, choices=STATUS_CHOICES)
    date = models.DateTimeField(u'Prašymo data', auto_now_add=True)
    user = models.ForeignKey(auth_models.User, verbose_name=u'Vartotojas')
    class Meta:
        verbose_name = u'Vartotojo suvesta informacija'
        verbose_name_plural = u'Vartototojų suvesta informacija'
