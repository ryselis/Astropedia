# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Constellation'
        db.create_table(u'cosmic_objects_constellation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
        ))
        db.send_create_signal(u'cosmic_objects', ['Constellation'])

        # Adding model 'AstronomicalObject'
        db.create_table(u'cosmic_objects_astronomicalobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cosmic_objects.Constellation'])),
            ('rectascence', self.gf('django.db.models.fields.FloatField')()),
            ('declination', self.gf('django.db.models.fields.FloatField')()),
            ('distance', self.gf('django.db.models.fields.FloatField')()),
            ('visible_magnitude', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'cosmic_objects', ['AstronomicalObject'])

        # Adding model 'ConstellationBound'
        db.create_table(u'cosmic_objects_constellationbound', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_rectascence', self.gf('django.db.models.fields.FloatField')()),
            ('end_rectascence', self.gf('django.db.models.fields.FloatField')()),
            ('start_declination', self.gf('django.db.models.fields.FloatField')()),
            ('end_declination', self.gf('django.db.models.fields.FloatField')()),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cosmic_objects.Constellation'])),
        ))
        db.send_create_signal(u'cosmic_objects', ['ConstellationBound'])

        # Adding model 'NebulaType'
        db.create_table(u'cosmic_objects_nebulatype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('sys_title', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'cosmic_objects', ['NebulaType'])

        # Adding model 'Star'
        db.create_table(u'cosmic_objects_star', (
            (u'astronomicalobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cosmic_objects.AstronomicalObject'], unique=True, primary_key=True)),
            ('absolute_magnitude', self.gf('django.db.models.fields.FloatField')()),
            ('spectral_class', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('brightness', self.gf('django.db.models.fields.FloatField')()),
            ('visible_magnitude_amplitude', self.gf('django.db.models.fields.FloatField')()),
            ('mass', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'cosmic_objects', ['Star'])

        # Adding model 'Galaxy'
        db.create_table(u'cosmic_objects_galaxy', (
            (u'astronomicalobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cosmic_objects.AstronomicalObject'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('galaxy_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('diameter', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'cosmic_objects', ['Galaxy'])

        # Adding model 'Nebula'
        db.create_table(u'cosmic_objects_nebula', (
            (u'astronomicalobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cosmic_objects.AstronomicalObject'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('nebula_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cosmic_objects.NebulaType'])),
        ))
        db.send_create_signal(u'cosmic_objects', ['Nebula'])

        # Adding model 'Planet'
        db.create_table(u'cosmic_objects_planet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('star', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cosmic_objects.Star'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('distance', self.gf('django.db.models.fields.FloatField')()),
            ('mass', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'cosmic_objects', ['Planet'])


    def backwards(self, orm):
        # Deleting model 'Constellation'
        db.delete_table(u'cosmic_objects_constellation')

        # Deleting model 'AstronomicalObject'
        db.delete_table(u'cosmic_objects_astronomicalobject')

        # Deleting model 'ConstellationBound'
        db.delete_table(u'cosmic_objects_constellationbound')

        # Deleting model 'NebulaType'
        db.delete_table(u'cosmic_objects_nebulatype')

        # Deleting model 'Star'
        db.delete_table(u'cosmic_objects_star')

        # Deleting model 'Galaxy'
        db.delete_table(u'cosmic_objects_galaxy')

        # Deleting model 'Nebula'
        db.delete_table(u'cosmic_objects_nebula')

        # Deleting model 'Planet'
        db.delete_table(u'cosmic_objects_planet')


    models = {
        u'cosmic_objects.astronomicalobject': {
            'Meta': {'object_name': 'AstronomicalObject'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.Constellation']"}),
            'declination': ('django.db.models.fields.FloatField', [], {}),
            'distance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'rectascence': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'visible_magnitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'cosmic_objects.constellation': {
            'Meta': {'object_name': 'Constellation'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'cosmic_objects.constellationbound': {
            'Meta': {'object_name': 'ConstellationBound'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.Constellation']"}),
            'end_declination': ('django.db.models.fields.FloatField', [], {}),
            'end_rectascence': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_declination': ('django.db.models.fields.FloatField', [], {}),
            'start_rectascence': ('django.db.models.fields.FloatField', [], {})
        },
        u'cosmic_objects.galaxy': {
            'Meta': {'object_name': 'Galaxy', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
            u'astronomicalobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosmic_objects.AstronomicalObject']", 'unique': 'True', 'primary_key': 'True'}),
            'diameter': ('django.db.models.fields.FloatField', [], {}),
            'galaxy_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'cosmic_objects.nebula': {
            'Meta': {'object_name': 'Nebula', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
            u'astronomicalobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosmic_objects.AstronomicalObject']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'nebula_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.NebulaType']"})
        },
        u'cosmic_objects.nebulatype': {
            'Meta': {'object_name': 'NebulaType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sys_title': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'cosmic_objects.planet': {
            'Meta': {'object_name': 'Planet'},
            'distance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'star': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.Star']"})
        },
        u'cosmic_objects.star': {
            'Meta': {'object_name': 'Star', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
            'absolute_magnitude': ('django.db.models.fields.FloatField', [], {}),
            u'astronomicalobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosmic_objects.AstronomicalObject']", 'unique': 'True', 'primary_key': 'True'}),
            'brightness': ('django.db.models.fields.FloatField', [], {}),
            'mass': ('django.db.models.fields.FloatField', [], {}),
            'spectral_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'visible_magnitude_amplitude': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['cosmic_objects']