# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2021-02-09 02:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210206_2043'),
        ('website', '0011_auto_20210206_2135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]