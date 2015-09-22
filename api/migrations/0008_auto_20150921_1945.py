# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150921_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['amount']},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='order',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='title',
            new_name='description',
        ),
    ]
