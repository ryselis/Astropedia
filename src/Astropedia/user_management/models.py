from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import models

# Create your models here.
class ScientistsAsks(models.Model):
    date = models.DateTimeField(u'Prašymo data', default=timezone.now)
    status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True)
    user = models.ForeignKey('User', verbose_name=u'Vartotojas')

class User(models.User):
	is_banned =  models.BooleanField(u'Ar uždraustas', default=False)

class UserSubmittedInfo(models.Model):
	odjecktId = IntegerField(u'Objekto Numeris')
	status = CharField(u'Statusas', max_length=1, null=False, blank=False, unique=True)
	date = models.DateTimeField(u'Prašymo data', default=timezone.now)
	user = models.ForeignKey('User', verbose_name=u'Vartotojas')

	class Ch

