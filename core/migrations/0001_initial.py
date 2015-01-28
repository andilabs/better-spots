# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Spot'
        db.create_table(u'core_spot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(max_length=40, null=True)),
            ('address_street', self.gf('django.db.models.fields.CharField')(default='', max_length=254)),
            ('address_number', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('address_city', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('address_country', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('spot_type', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('is_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('www', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('is_enabled', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('friendly_rate', self.gf('django.db.models.fields.DecimalField')(default=-1.0, null=True, max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'core', ['Spot'])

        # Adding model 'Raiting'
        db.create_table(u'core_raiting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.SpotUser'])),
            ('spot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Spot'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')()),
            ('friendly_rate', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['Raiting'])

        # Adding unique constraint on 'Raiting', fields ['user', 'spot']
        db.create_unique(u'core_raiting', ['user_id', 'spot_id'])

        # Adding model 'Opinion'
        db.create_table(u'core_opinion', (
            ('raiting', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Raiting'], unique=True, primary_key=True)),
            ('opinion_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'core', ['Opinion'])

        # Adding model 'OpinionUsefulnessRating'
        db.create_table(u'core_opinionusefulnessrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opinion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Opinion'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.SpotUser'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
        ))
        db.send_create_signal(u'core', ['OpinionUsefulnessRating'])

        # Adding model 'UsersSpotsList'
        db.create_table(u'core_usersspotslist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('spot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Spot'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.SpotUser'])),
            ('role', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
        ))
        db.send_create_signal(u'core', ['UsersSpotsList'])


    def backwards(self, orm):
        # Removing unique constraint on 'Raiting', fields ['user', 'spot']
        db.delete_unique(u'core_raiting', ['user_id', 'spot_id'])

        # Deleting model 'Spot'
        db.delete_table(u'core_spot')

        # Deleting model 'Raiting'
        db.delete_table(u'core_raiting')

        # Deleting model 'Opinion'
        db.delete_table(u'core_opinion')

        # Deleting model 'OpinionUsefulnessRating'
        db.delete_table(u'core_opinionusefulnessrating')

        # Deleting model 'UsersSpotsList'
        db.delete_table(u'core_usersspotslist')


    models = {
        u'accounts.spotuser': {
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
        u'core.opinion': {
            'Meta': {'object_name': 'Opinion'},
            'opinion_text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'raiting': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Raiting']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.opinionusefulnessrating': {
            'Meta': {'object_name': 'OpinionUsefulnessRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Opinion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'core.raiting': {
            'Meta': {'unique_together': "(('user', 'spot'),)", 'object_name': 'Raiting'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friendly_rate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"})
        },
        u'core.spot': {
            'Meta': {'object_name': 'Spot'},
            'address_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'address_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'address_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'address_street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '254'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'friendly_rate': ('django.db.models.fields.DecimalField', [], {'default': '-1.0', 'null': 'True', 'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_enabled': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'spot_type': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'core.usersspotslist': {
            'Meta': {'object_name': 'UsersSpotsList'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"})
        }
    }

    complete_apps = ['core']