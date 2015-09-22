# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20150921_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('album', models.ForeignKey(related_name='items', to='api.Invoice')),
            ],
            options={
                'ordering': ['amount'],
            },
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
