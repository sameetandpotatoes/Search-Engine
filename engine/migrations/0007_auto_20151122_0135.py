# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_auto_20151115_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
