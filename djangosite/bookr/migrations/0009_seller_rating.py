# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0008_auto_20160419_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
