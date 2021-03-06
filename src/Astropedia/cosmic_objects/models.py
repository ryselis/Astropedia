# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.files import FileField

# Create your models here.
from user_management.models import UserSubmittedInfo


class Constellation(models.Model):
    name = CharField(u'Pavadinimas', max_length=32, null=False, blank=False)
    abbreviation = CharField(u'Santrumpa', max_length=8, null=False, blank=False,
                             unique=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Žvaigždynas'
        verbose_name_plural = u'Žvaigždynai'


class AstronomicalObject(models.Model):
    TYPE_STAR = '0'
    constellation = ForeignKey(u'Constellation', verbose_name='Žvaigždynas')
    rectascence = FloatField(u'Rektascencija')
    declination = FloatField(u'Deklinacija')
    distance = FloatField(u'Atstumas')
    visible_magnitude = FloatField(u'Regimasis ryškis')
    name = CharField(u'Pavadinimas', max_length=32, null=False, blank=True)
    type = CharField(u'Tipas', max_length=32, editable=False)
    user_submission = ForeignKey(UserSubmittedInfo, verbose_name=u'Vartotojo pateikta info', null=True, editable=False)

    class Meta:
        ordering = ['visible_magnitude']
        verbose_name = u'Astronominis objektas'
        verbose_name_plural = u'Astronominiai objektai'

    def __unicode__(self):
        return self.name

class ConstellationBound(models.Model):
    start_rectascence = FloatField(u'Pradžios rekstascencija')
    end_rectascence = FloatField(u'Pabaigos rekstascencija')
    start_declination = FloatField(u'Pradžios deklinacija')
    end_declination = FloatField(u'Pabaigos deklinacija')
    constellation = ForeignKey('Constellation', verbose_name=u'Žvaigždynas')

    def __unicode__(self):
        return u"Rėžis " + self.constellation.name

    class Meta:
        verbose_name = u'Žvaigždyno rėžis'
        verbose_name_plural = u'Žvaigždyno rėžiai'
    
class NebulaType(models.Model):
    name = CharField(u'Pavadinimas', max_length=32)
    sys_title = CharField(u'Sisteminis raktas', max_length=4)

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = u'Ūko tipas'
        verbose_name_plural = u'Ūko tipai'
    
class Star(AstronomicalObject):
    absolute_magnitude = FloatField(u'Absoliutinis ryškis')
    spectral_class = CharField(u'Spektrinė klasė', max_length=10)
    brightness = FloatField(u'Šviesis')
    visible_magnitude_amplitude = FloatField(u'Regimojo ryškio kitimo amplitudė')
    mass = FloatField(u'Masė')

    def get_submission_status(self):
        if self.user_submission:
            return self.user_submission.get_status_display()
        return u''
    get_submission_status.short_description = u'Patvirtinimo būsena'

    class Meta:
        verbose_name = u'Žvaigždė'
        verbose_name_plural = u'Žvaigždės'
    
class Galaxy(AstronomicalObject):
    image = FileField(u'Paveikslėlis', upload_to='images', null=True, blank=True)
    galaxy_type = CharField(u'Galaktikos tipas', max_length=16)
    diameter = FloatField(u'Skersmuo')

    class Meta:
        verbose_name = u'Galaktika'
        verbose_name_plural = u'Galaktikos'
    
class Nebula(AstronomicalObject):
    image = FileField(u'Paveikslėlis', upload_to='images',null=True, blank=True)
    nebula_type = ForeignKey('NebulaType', verbose_name=u'Ūko tipas',
                             )

    class Meta:
        verbose_name = u'Ūkas'
        verbose_name_plural = u'Ūkai'

class Planet(models.Model):
    star = ForeignKey('Star', verbose_name=u'Žvaigždė')
    name = CharField(u'Pavadinimas', max_length=32)
    distance = FloatField(u'Atstumas iki žvaigždės')
    mass = FloatField(u'Masė')
    user_submission = ForeignKey(UserSubmittedInfo, verbose_name=u'Vartotojo pateikta info', null=True,
                                 editable=False)

    def __unicode__(self):
        return unicode(self.star) + ":" + self.name

    class Meta:
        verbose_name = u'Planeta'
        verbose_name_plural = u'Planetos'
