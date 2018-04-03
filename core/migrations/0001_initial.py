# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 12:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields

from utils.img_path import get_image_path

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('slogan', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('main_color', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('description', models.TextField()),
                ('windows_phone_store_url', models.URLField(blank=True, max_length=1023, null=True)),
                ('google_store_url', models.URLField(blank=True, max_length=1023, null=True)),
                ('apple_store_url', models.URLField(blank=True, max_length=1023, null=True)),
                ('instagram', models.CharField(blank=True, max_length=254, null=True)),
                ('facebook', models.CharField(blank=True, max_length=254, null=True)),
                ('twitter', models.CharField(blank=True, max_length=254, null=True)),
                ('blogger_photo', models.ImageField(blank=True, null=True, upload_to=get_image_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpinionUsefulnessRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('vote', models.IntegerField(choices=[(1, 'Upvote'), (-1, 'Downvote')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_enabled', models.BooleanField(choices=[(False, 'Not allowed'), (True, 'Allowed')], default=False)),
                ('friendly_rate', models.PositiveIntegerField(choices=[(1, 'terrible'), (2, 'poor'), (3, 'average'), (4, 'very good'), (5, 'excellent')])),
            ],
            options={
                'abstract': False,
            }
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=250)),
                ('location', django.contrib.gis.db.models.fields.PointField(max_length=40, srid=4326)),
                ('address_street', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('address_number', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('address_city', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address_country', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('spot_type', models.IntegerField(choices=[(1, 'cafe'), (2, 'restaurant'), (3, 'hotel'), (4, 'shop-no-food'), (5, 'shop-with-food')])),
                ('is_accepted', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('www', models.URLField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=254, null=True)),
                ('is_enabled', models.NullBooleanField(default=None)),
                ('friendly_rate', models.DecimalField(decimal_places=2, default=-1.0, max_digits=3, null=True)),
                ('is_certificated', models.BooleanField(default=False)),
                ('venue_photo', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to=get_image_path)),
                ('cropping_venue_photo', image_cropping.fields.ImageRatioField('venue_photo', '350x150', adapt_rotation=False,
                                                                               allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False,
                                                                               size_warning=True, verbose_name='cropping venue photo')),
                ('spot_slug', models.SlugField(max_length=1000)),
                ('anonymous_creator_cookie', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('opinion_text', models.CharField(max_length=500)),
                ('rating', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Rating')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.Spot'),
        ),
        migrations.AddField(
            model_name='opinionusefulnessrating',
            name='opinion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Opinion'),
        ),
    ]
