# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20151214_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 37, 4, 837167, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='instructor',
            field=models.ForeignKey(null=True, to='instructors.Instructor'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='student',
            field=models.ForeignKey(to='students.Student', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentinstructor',
            name='apply_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 37, 4, 836166, tzinfo=utc)),
        ),
    ]
