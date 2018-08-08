# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-08 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('image', models.ImageField(default=b'img/blog/thumbnail-default.jpg', upload_to=b'events')),
                ('venue', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=2024, unique=True)),
                ('club', models.CharField(blank=True, choices=[(b'codeschool', b'Codeschool'), (b'cogitans', b'Cogitans'), (b'droidclub', b'Droid Club'), (b'ecell', b'E-Cell'), (b'electrotech', b'Electrotech'), (b'oslc', b'OSLC'), (b'renderedusict', b'Rendered-USICT'), (b'turingai', b'Turing A.I.')], max_length=200)),
            ],
        ),
    ]
