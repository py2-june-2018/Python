# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-22 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='SOME STRING'),
        ),
    ]