# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 23:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import website.models
import members.models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '\u200b\u200b\u200b\u200b\u200b\u200b\u200bDepartments',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('affiliation', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=website.models.get_default_time)),
                ('location', models.CharField(default=website.models.get_default_room, max_length=200)),
                ('cancelled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='IQUISE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=2000)),
                ('default_location', models.CharField(default='MIT Room 26-214', max_length=200)),
                ('default_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'iQuISE',
                'verbose_name_plural': '\u200biQuISE',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', members.models.EmailIField(blank=True, max_length=254)),
                ('MIT_ID', models.PositiveIntegerField(blank=True, null=True, verbose_name='MIT ID')),
                ('year', models.CharField(blank=True, help_text='Sophomore, Graduate Year #, Postdoc, Professor, etc.', max_length=10)),
                ('lab', models.CharField(blank=True, max_length=200)),
                ('subscribed', models.BooleanField(default=False, help_text='iquise-associates@mit.edu')),
                ('join_method', models.CharField(choices=[('manual', 'Manual Entry'), ('website', 'Requested on Website'), ('moira', 'Joined through Moira'), ('id', 'MIT ID')], default='manual', max_length=20)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Department')),
            ],
            options={
                'ordering': ['-last_name', '-first_name'],
                'verbose_name_plural': '\u200b\u200b\u200b\u200b\u200bPeople',
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='TBD', max_length=200)),
                ('short_description', models.CharField(default='TBD', max_length=500)),
                ('long_description', models.TextField(default='TBD', max_length=10000)),
                ('supp_url', models.URLField(blank=True, verbose_name='supplemental url')),
                ('theme', models.CharField(choices=[('EXPERIMENT', 'Experimental'), ('THEORY', 'Theoretical')], default='EXPERIMENT', max_length=20)),
                ('confirmed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Event')),
            ],
            options={
                'ordering': ['-event__date'],
                'verbose_name_plural': '\u200b\u200b\u200bPresentations',
            },
        ),
        migrations.CreateModel(
            name='Presenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('affiliation', models.CharField(max_length=200)),
                ('profile_image_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name_plural': '\u200b\u200b\u200b\u200bPresenters',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=200)),
                ('school_status', models.CharField(blank=True, max_length=200)),
                ('profile_image_url', models.URLField(blank=True)),
                ('further_info_url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '\u200b\u200b\u200b\u200b\u200b\u200bSchools',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Label for the session, e.g. "Fall 2018"', max_length=50, unique=True)),
                ('start', models.DateField()),
                ('stop', models.DateField()),
                ('slug', models.SlugField(help_text='Appears in URLs')),
            ],
            options={
                'ordering': ['-start'],
                'verbose_name': 'Session',
                'verbose_name_plural': '\u200b\u200bSessions (event organizer)',
            },
        ),
        migrations.AddField(
            model_name='presentation',
            name='presenters',
            field=models.ManyToManyField(to='website.Presenter'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='primary_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.School'),
        ),
        migrations.AddField(
            model_name='event',
            name='audience',
            field=models.ManyToManyField(blank=True, to='website.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Donor'),
        ),
    ]
