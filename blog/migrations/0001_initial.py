# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 12:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields
from utils.img_path import get_image_path


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(help_text='blog note text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, help_text='Saving with empty values makes post unpublished', null=True)),
                ('photo', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to=get_image_path)),
                ('cropping_photo', image_cropping.fields.ImageRatioField('photo', '2402x2402', adapt_rotation=False, allow_fullsize=False, free_crop=False,
                                                                         help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping photo')),
                ('post_slug', models.SlugField(max_length=1200)),
                ('spot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='core.Spot')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
