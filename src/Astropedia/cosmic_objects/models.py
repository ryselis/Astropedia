from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey

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