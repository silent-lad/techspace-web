# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170909_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='blog/thumbnail-default.jpg', upload_to='blog'),
        ),
    ]