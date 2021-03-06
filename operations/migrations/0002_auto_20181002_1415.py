# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-02 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(help_text='Assingn Department (or project to user, The Dept Head defined in Department Table would be the person managing the records of specific employee.', on_delete=django.db.models.deletion.CASCADE, to='operations.Department'),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='to_date',
            field=models.DateField(),
        ),
    ]
