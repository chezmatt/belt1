# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0002_auto_20170127_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=75, null=True, unique=True),
        ),
    ]
