# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='person',
            field=models.ForeignKey(to='users.Person', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='apply_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 6, 59, 56, 245233, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 6, 59, 56, 244232, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentinstructor',
            name='apply_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 6, 59, 56, 243231, tzinfo=utc)),
        ),
    ]
