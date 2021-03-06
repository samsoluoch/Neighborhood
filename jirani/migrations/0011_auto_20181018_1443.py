# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0010_auto_20181018_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='business',
            old_name='location',
            new_name='neighborhood',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='occupants',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jirani.Location'),
        ),
    ]
