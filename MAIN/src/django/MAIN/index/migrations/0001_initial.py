# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='task')),
                ('is_resolved', models.BooleanField(verbose_name='Resolved?')),
            ],
        ),
    ]
