# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaperUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='昵称', max_length=20, default='')),
                ('passwd', models.CharField(verbose_name='密码', max_length=20, default='ad123456')),
                ('email', models.EmailField(verbose_name='邮箱', max_length=50)),
            ],
        ),
    ]
