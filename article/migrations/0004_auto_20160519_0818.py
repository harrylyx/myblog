# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160519_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='shortContent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]