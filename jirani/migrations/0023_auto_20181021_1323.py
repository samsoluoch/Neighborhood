# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0022_auto_20181021_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='hospital',
            field=models.TextField(default='999'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='police',
            field=models.TextField(default='999'),
        ),
    ]