# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.files import FileField

# Create your models here.

class Constellation(models.Model):
    name = CharField(u'Pavadinimas', max_length=32, null=False, blank=False)
    abbreviation = CharField(u'Santrumpa', max_length=8, null=False, blank=False,
                             unique=True)
    
class AstronomicalObject(models.Model):
    constellation = ForeignKey(u'Constellation', verbose_name='Žvaigždynas')
    rectascence = FloatField(u'Rektascencija')
    declination = FloatField(u'Deklinacija')
    distance = FloatField(u'Atstumas')
    visible_magnitude = FloatField(u'Regimasis ryškis')
    name = CharField(u'Pavadinimas', max_length=32, null=False, blank=True)
    type = CharField(u'Tipas', max_length=32)
    
class ConstellationBound(models.Model):
    start_rectascence = FloatField(u'Pradžios rekstascencija')
    end_rectascence = FloatField(u'Pabaigos rekstascencija')
    start_declination = FloatField(u'Pradžios deklinacija')
    end_declination = FloatField(u'Pabaigos deklinacija')
    constellation = ForeignKey('Constellation', verbose_name=u'Žvaigždynas')
    
class NebulaType(models.Model):
    name = CharField(u'Pavadinimas', max_length=32)
    sys_title = CharField(u'Sisteminis raktas', max_length=4)
    
class Star(AstronomicalObject):
    absolute_magnitude = FloatField(u'Absoliutinis ryškis')
    spectral_class = CharField(u'Spektrinė klasė', max_length=10)
    brightness = FloatField(u'Šviesis')
    visible_magnitude_amplitude = FloatField(u'Regimojo ryškio kitimo amplitudė')
    mass = FloatField(u'Masė')
    
class Galaxy(AstronomicalObject):
    image = FileField(u'Paveikslėlis', upload_to='images')
    galaxy_type = CharField(u'Galaktikos tipas', max_length=16)
    diameter = FloatField(u'Skersmuo')
    
class Nebula(AstronomicalObject):
    image = FileField(u'Paveikslėlis', upload_to='images')
    nebula_type = ForeignKey('NebulaType', verbose_name=u'Ūko tipas')
     
class Planet(models.Model):
    star = ForeignKey('Star', verbose_name=u'Žvaigždė')
    name = CharField(u'Pavadinimas', max_length=32)
    distance = FloatField(u'Atstumas iki žvaigždės')
    mass = FloatField(u'Masė')
    