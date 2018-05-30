# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('temperature', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('warning', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='default.User'),
        ),
    ]