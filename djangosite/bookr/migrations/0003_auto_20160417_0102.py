# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0002_auto_20160417_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('PH', 'Phone'), ('EM', 'Email')], default='PH', max_length=2),
        ),
    ]
