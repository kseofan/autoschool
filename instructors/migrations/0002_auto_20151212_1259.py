# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='user',
        ),
        migrations.AddField(
            model_name='instructor',
            name='person',
            field=models.ForeignKey(to='users.Person', null=True),
        ),
    ]
