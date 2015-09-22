# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150921_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RenameModel(
            old_name='Album',
            new_name='Invoice',
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.AddField(
            model_name='item',
            name='album',
            field=models.ForeignKey(related_name='items', to='api.Invoice'),
        ),
    ]
