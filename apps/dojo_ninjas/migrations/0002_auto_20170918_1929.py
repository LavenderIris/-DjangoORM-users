# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-18 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dojo',
            old_name='first_name',
            new_name='name',
        ),
    ]
