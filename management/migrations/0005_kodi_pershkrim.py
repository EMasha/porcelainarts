# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-22 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20180622_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='kodi',
            name='pershkrim',
            field=models.TextField(blank=True, null=True),
        ),
    ]
