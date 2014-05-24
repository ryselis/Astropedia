from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Constellation(models.Model):
    name = CharField('Pavadinimas', max_length=32, null=False, blank=False)
    abbreviation = CharField('Santrumpa', max_length=8, null=False, blank=False,
                             unique=True)
    
class AstronomicalObject(models.Model):
    constellation = ForeignKey('Constellation', verbose_name='Žvaigždynas')
    rectascence = FloatField('Rektascencija')
    declination = FloatField('Deklinacija')
    distance = FloatField('Atstumas')
    visible_magnitude = FloatField('Regimasis ryškis')
    name = CharField('')