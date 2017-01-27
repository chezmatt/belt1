# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import version1.models


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=75, null=True, unique=True, validators=[version1.models.User.validateUsername]),
        ),
    ]
