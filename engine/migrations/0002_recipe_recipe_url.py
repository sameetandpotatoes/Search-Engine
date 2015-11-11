# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_url',
            field=models.TextField(default='http://allrecipes.net', max_length=2000),
            preserve_default=False,
        ),
    ]
