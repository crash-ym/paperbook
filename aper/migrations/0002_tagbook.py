# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tagId', models.BinaryField(verbose_name='TAGid', max_length=8, default='')),
                ('tagName', models.CharField(verbose_name='标签', max_length=8, default='默认')),
            ],
        ),
    ]
