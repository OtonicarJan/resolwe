# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-13 08:19
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0009_data_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptorschema',
            name='schema',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]
