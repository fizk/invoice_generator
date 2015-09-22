# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='track',
            name='duration',
        ),
    ]
