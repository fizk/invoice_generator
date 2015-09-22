# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150921_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['description']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='album',
            new_name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='album_name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.AddField(
            model_name='invoice',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='first_name',
            field=models.CharField(default='J\xfal\xeda', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='last_name',
            field=models.CharField(default='Ilin', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='Bitcoin', max_length=256),
            preserve_default=False,
        ),
    ]
