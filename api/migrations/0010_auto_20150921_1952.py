# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20150921_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='album',
            name='country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='currency',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
