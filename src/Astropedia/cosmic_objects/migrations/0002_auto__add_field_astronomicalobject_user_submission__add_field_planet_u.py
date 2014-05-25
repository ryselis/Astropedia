# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AstronomicalObject.user_submission'
        db.add_column(u'cosmic_objects_astronomicalobject', 'user_submission',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_management.UserSubmittedInfo'], null=True),
                      keep_default=False)

        # Adding field 'Planet.user_submission'
        db.add_column(u'cosmic_objects_planet', 'user_submission',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_management.UserSubmittedInfo'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AstronomicalObject.user_submission'
        db.delete_column(u'cosmic_objects_astronomicalobject', 'user_submission_id')

        # Deleting field 'Planet.user_submission'
        db.delete_column(u'cosmic_objects_planet', 'user_submission_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cosmic_objects.astronomicalobject': {
            'Meta': {'ordering': "['visible_magnitude']", 'object_name': 'AstronomicalObject'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.Constellation']"}),
            'declination': ('django.db.models.fields.FloatField', [], {}),
            'distance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'rectascence': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user_submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_management.UserSubmittedInfo']", 'null': 'True'}),
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
            'Meta': {'ordering': "['visible_magnitude']", 'object_name': 'Galaxy', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
            u'astronomicalobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosmic_objects.AstronomicalObject']", 'unique': 'True', 'primary_key': 'True'}),
            'diameter': ('django.db.models.fields.FloatField', [], {}),
            'galaxy_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'cosmic_objects.nebula': {
            'Meta': {'ordering': "['visible_magnitude']", 'object_name': 'Nebula', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
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
            'star': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosmic_objects.Star']"}),
            'user_submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_management.UserSubmittedInfo']", 'null': 'True'})
        },
        u'cosmic_objects.star': {
            'Meta': {'ordering': "['visible_magnitude']", 'object_name': 'Star', '_ormbases': [u'cosmic_objects.AstronomicalObject']},
            'absolute_magnitude': ('django.db.models.fields.FloatField', [], {}),
            u'astronomicalobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosmic_objects.AstronomicalObject']", 'unique': 'True', 'primary_key': 'True'}),
            'brightness': ('django.db.models.fields.FloatField', [], {}),
            'mass': ('django.db.models.fields.FloatField', [], {}),
            'spectral_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'visible_magnitude_amplitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'user_management.usersubmittedinfo': {
            'Meta': {'object_name': 'UserSubmittedInfo'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'odjecktId': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['cosmic_objects']