# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-12 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_userprofile_bstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sprite',
            field=models.CharField(choices=[('girl', 'girl'), ('boy', 'boy')], default='Null', max_length=50),
        ),
    ]