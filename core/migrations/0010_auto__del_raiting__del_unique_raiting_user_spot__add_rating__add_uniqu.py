# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Raiting', fields ['user', 'spot']
        db.delete_unique(u'core_raiting', ['user_id', 'spot_id'])

        # Deleting model 'Raiting'
        db.delete_table(u'core_raiting')

        # Adding model 'Rating'
        db.create_table(u'core_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.SpotUser'])),
            ('spot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Spot'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friendly_rate', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('facilities', self.gf(u'django_hstore.fields.DictionaryField')(default=None, null=True)),
        ))
        db.send_create_signal(u'core', ['Rating'])

        # Adding unique constraint on 'Rating', fields ['user', 'spot']
        db.create_unique(u'core_rating', ['user_id', 'spot_id'])


        # Changing field 'Opinion.rating'
        db.alter_column(u'core_opinion', 'rating_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Rating'], unique=True, primary_key=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Rating', fields ['user', 'spot']
        db.delete_unique(u'core_rating', ['user_id', 'spot_id'])

        # Adding model 'Raiting'
        db.create_table(u'core_raiting', (
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('facilities', self.gf(u'django_hstore.fields.DictionaryField')(default=None, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.SpotUser'])),
            ('friendly_rate', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('spot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Spot'])),
            ('data_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Raiting'])

        # Adding unique constraint on 'Raiting', fields ['user', 'spot']
        db.create_unique(u'core_raiting', ['user_id', 'spot_id'])

        # Deleting model 'Rating'
        db.delete_table(u'core_rating')


        # Changing field 'Opinion.rating'
        db.alter_column(u'core_opinion', 'rating_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Raiting'], unique=True, primary_key=True))

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
            'rating': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Rating']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.opinionusefulnessrating': {
            'Meta': {'object_name': 'OpinionUsefulnessRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Opinion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'core.rating': {
            'Meta': {'unique_together': "(('user', 'spot'),)", 'object_name': 'Rating'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facilities': (u'django_hstore.fields.DictionaryField', [], {u'default': None, 'null': 'True'}),
            'friendly_rate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"})
        },
        u'core.spot': {
            'Meta': {'object_name': 'Spot'},
            'address_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'cropping_venue_photo': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'facilities': (u'django_hstore.fields.DictionaryField', [], {u'default': None, 'null': 'True'}),
            'friendly_rate': ('django.db.models.fields.DecimalField', [], {'default': '-1.0', 'null': 'True', 'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_certificated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_enabled': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spot_slug': ('django.db.models.fields.SlugField', [], {'max_length': '1000'}),
            'spot_type': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'venue_photo': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'core.usersspotslist': {
            'Meta': {'unique_together': "(('user', 'spot', 'role'),)", 'object_name': 'UsersSpotsList'},
            'data_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Spot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.SpotUser']"})
        }
    }

    complete_apps = ['core']