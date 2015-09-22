# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20150921_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='album',
            new_name='invoice',
        ),
    ]
