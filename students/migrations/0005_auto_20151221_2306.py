# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20151218_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='is_cancelable',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 21, 17, 6, 14, 100223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentinstructor',
            name='apply_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 21, 17, 6, 14, 99224, tzinfo=utc)),
        ),
    ]
