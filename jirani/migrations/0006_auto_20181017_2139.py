# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0005_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='hospital',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='police',
            field=models.TextField(null=True),
        ),
    ]
