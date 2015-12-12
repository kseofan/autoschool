# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('middle_name', models.TextField(blank=True, null=True)),
                ('dateOfBirth', models.DateTimeField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(default=0, choices=[(0, 'Student'), (1, 'Instructor'), (2, 'Curator')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
