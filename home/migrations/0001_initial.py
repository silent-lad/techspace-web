# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=255)),
                ('captain', models.CharField(default='null', max_length=255)),
                ('club_image', models.ImageField(upload_to='logo')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('app_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]