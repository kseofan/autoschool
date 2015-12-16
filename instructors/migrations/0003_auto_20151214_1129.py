# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_auto_20151212_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='person',
            field=models.ForeignKey(unique=True, to='users.Person', null=True),
        ),
    ]
