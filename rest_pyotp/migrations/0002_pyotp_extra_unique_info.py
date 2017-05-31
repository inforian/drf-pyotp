# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_pyotp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyotp',
            name='extra_unique_info',
            field=models.CharField(blank=True, help_text='Extra uniqoue info regarding OTp (custom requirement for v3)', max_length=255, null=True, verbose_name='Extra Unique Info'),
        ),
    ]