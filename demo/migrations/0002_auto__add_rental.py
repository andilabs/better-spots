# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rental'
        db.create_table(u'demo_rental', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django_google_maps.fields.AddressField')(max_length=200)),
            ('geolocation', self.gf('django_google_maps.fields.GeoLocationField')(max_length=100)),
        ))
        db.send_create_signal(u'demo', ['Rental'])


    def backwards(self, orm):
        # Deleting model 'Rental'
        db.delete_table(u'demo_rental')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'demo.emailverification': {
            'Meta': {'object_name': 'EmailVerification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.SpotUser']"}),
            'verification_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '21'})
        },
        u'demo.opinion': {
            'Meta': {'object_name': 'Opinion'},
            'opinion_text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'raiting': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['demo.Raiting']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.opinionusefulnessrating': {
            'Meta': {'object_name': 'OpinionUsefulnessRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.Opinion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.SpotUser']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'demo.raiting': {
            'Meta': {'unique_together': "(('user', 'spot'),)", 'object_name': 'Raiting'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dogs_allowed': ('django.db.models.fields.BooleanField', [], {}),
            'friendly_rate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.SpotUser']"})
        },
        u'demo.rental': {
            'Meta': {'object_name': 'Rental'},
            'address': ('django_google_maps.fields.AddressField', [], {'max_length': '200'}),
            'geolocation': ('django_google_maps.fields.GeoLocationField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'demo.spot': {
            'Meta': {'object_name': 'Spot'},
            'address_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'address_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'address_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'address_street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '254'}),
            'dogs_allowed': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'friendly_rate': ('django.db.models.fields.DecimalField', [], {'default': '-1.0', 'null': 'True', 'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'spot_type': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'demo.spotuser': {
            'Meta': {'object_name': 'SpotUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'mail_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'demo.usersspotslist': {
            'Meta': {'object_name': 'UsersSpotsList'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.SpotUser']"})
        }
    }

    complete_apps = ['demo']