# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-20 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_manager', '0011_auto_20170311_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('order', models.IntegerField(default=0)),
                ('zoom', models.IntegerField(blank=True, default=None, null=True)),
                ('x_coord', models.FloatField(blank=True, default=None, null=True)),
                ('y_coord', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LayerState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('opacity', models.FloatField(default=1.0)),
                ('focus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rea.Focus')),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_manager.Layer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('order', models.IntegerField(default=0)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rea.Header')),
            ],
        ),
        migrations.AddField(
            model_name='focus',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rea.Topic'),
        ),
    ]