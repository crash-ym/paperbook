# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aper', '0003_tagbook_tagbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('authorName', models.CharField(verbose_name='作家名字', max_length=50, default='')),
                ('contry', models.CharField(verbose_name='国籍', max_length=20, default='Earth')),
                ('describ', models.CharField(verbose_name='描述', max_length=500, default='暂无简介')),
                ('masterpiece', models.CharField(verbose_name='代表作', max_length=200, default='暂无记录')),
                ('link', models.CharField(verbose_name='详细链接', max_length=100, default='暂无链接')),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bookName', models.CharField(verbose_name='书名', max_length=50, default='')),
                ('authorName', models.CharField(verbose_name='作者', max_length=50, default='佚名')),
                ('bookTag', models.CharField(verbose_name='标签', max_length=8, default='暂无标签')),
                ('bookLink', models.CharField(verbose_name='链接', max_length=200, default='暂无链接')),
                ('bookDes', models.CharField(verbose_name='书籍描述', max_length=500, default='暂无描述')),
            ],
        ),
    ]
