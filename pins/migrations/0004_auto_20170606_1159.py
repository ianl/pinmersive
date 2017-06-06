# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-06 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0003_pin_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to='boards.Board'),
        ),
    ]
