# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20150921_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='invoice',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
