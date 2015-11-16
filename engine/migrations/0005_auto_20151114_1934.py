# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20151114_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
