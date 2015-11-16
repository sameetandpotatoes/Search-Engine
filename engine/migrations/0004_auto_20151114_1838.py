# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_auto_20151111_1912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
