# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-26 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='site',
        ),
        migrations.DeleteModel(
            name='SocialMediaSettings',
        ),
    ]