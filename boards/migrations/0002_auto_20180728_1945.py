# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-28 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='users.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='board',
            unique_together=set([('user_profile', 'name')]),
        ),
    ]
