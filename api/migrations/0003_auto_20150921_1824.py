# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150921_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
