# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PSost',
            new_name='Post',
        ),
    ]
