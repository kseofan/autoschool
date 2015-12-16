# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151212_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='application',
            name='student',
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_cancelable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='student',
            field=models.ForeignKey(null=True, to='students.Student'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 5, 29, 18, 244992, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='person',
            field=models.ForeignKey(unique=True, to='users.Person', null=True),
        ),
        migrations.AlterField(
            model_name='studentinstructor',
            name='apply_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 5, 29, 18, 243986, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
