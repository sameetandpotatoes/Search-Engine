# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_recipe_recipe_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='title',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_url',
            field=models.TextField(unique=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
