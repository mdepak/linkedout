# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-14 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20180114_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsapplied',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.CompanyJobs'),
        ),
    ]