# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('apply_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 10, 10, 37, 3, 504789, tzinfo=utc))),
                ('is_actual', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 10, 10, 37, 3, 504789, tzinfo=utc))),
                ('hours', models.IntegerField(default=0)),
                ('instructor', models.ForeignKey(to='instructors.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('middle_name', models.TextField(blank=True, null=True)),
                ('dateOfBirth', models.DateTimeField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('applications_limit', models.IntegerField(default=10)),
                ('skill_level', models.IntegerField(choices=[(0, 'Unfamiliar'), (1, 'Familiar'), (2, 'Experienced')], default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentInstructor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('apply_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 10, 10, 37, 3, 503787, tzinfo=utc))),
                ('instructor', models.ForeignKey(to='instructors.Instructor')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='lesson',
            field=models.ForeignKey(to='students.Lesson'),
        ),
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
    ]
