# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('curators', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curator',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='curator',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='curator',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='curator',
            name='user',
        ),
        migrations.AddField(
            model_name='curator',
            name='person',
            field=models.ForeignKey(to='users.Person', null=True),
        ),
    ]
