# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0021_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='jirani.Neighborhood'),
        ),
    ]
