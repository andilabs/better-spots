# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields
import utils.img_path


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(help_text='blog note text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, help_text='Saving with empty values makes post unpublished', null=True)),
                ('blogpost_photo', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to=utils.img_path.get_image_path)),
                ('cropping_blogpost_photo', image_cropping.fields.ImageRatioField('blogpost_photo', '2402x2402', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping blogpost photo')),
                ('post_slug', models.SlugField(max_length=1200)),
                ('spot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='core.Spot')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
