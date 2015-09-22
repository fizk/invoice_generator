# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150921_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=256, null=True)),
                ('country', models.CharField(max_length=256, null=True)),
                ('email', models.CharField(max_length=256, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('currency', models.CharField(max_length=256, null=True)),
                ('closed', models.BooleanField(default=False)),
                ('success', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(related_name='items', to='api.Invoice'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
