# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-12-28 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0004_auto_20201228_1247'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='committeemembership',
            unique_together=set([('user', 'committee')]),
        ),
    ]