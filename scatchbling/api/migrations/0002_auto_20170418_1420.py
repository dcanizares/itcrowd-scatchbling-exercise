# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-18 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsize',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemsize',
            name='size',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ItemSize',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
