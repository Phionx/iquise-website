# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-12-20 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20201212_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='audience',
        ),
    ]
