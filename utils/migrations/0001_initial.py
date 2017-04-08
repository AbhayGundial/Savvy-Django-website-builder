# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-26 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text=b'Your Facebook page URL', null=True)),
                ('instagram', models.URLField(blank=True, help_text=b'Your Instagram URL', max_length=255, null=True)),
                ('twitter_name', models.URLField(blank=True, help_text=b'Your Twitter URL', max_length=255, null=True)),
                ('youtube', models.URLField(blank=True, help_text=b'Your YouTube Channel URL', null=True)),
                ('linkedin', models.URLField(blank=True, help_text=b'Your Linkedin URL', max_length=255, null=True)),
                ('github', models.URLField(blank=True, help_text=b'Your Github URL', max_length=255, null=True)),
                ('facebook_appid', models.CharField(blank=True, help_text=b'Your Facbook AppID', max_length=255, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
