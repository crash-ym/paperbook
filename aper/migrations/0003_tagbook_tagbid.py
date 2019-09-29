# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aper', '0002_tagbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagbook',
            name='tagBid',
            field=models.CharField(verbose_name='TAGBid', max_length=8, default=''),
        ),
    ]
