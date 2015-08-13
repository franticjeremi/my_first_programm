# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('dataType', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('example', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mymarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WidgetExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=2000)),
                ('widget', models.ForeignKey(to='mymarket.Mymarket')),
            ],
        ),
        migrations.AddField(
            model_name='method',
            name='widget',
            field=models.ForeignKey(to='mymarket.Mymarket'),
        ),
        migrations.AddField(
            model_name='event',
            name='widget',
            field=models.ForeignKey(to='mymarket.Mymarket'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='widget',
            field=models.ForeignKey(to='mymarket.Mymarket'),
        ),
    ]
