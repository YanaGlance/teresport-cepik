# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('reg_no', models.CharField(max_length=8)),
                ('model', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('production_year', models.DateField()),
                ('engine_number', models.CharField(max_length=20)),
                ('engine_capacity', models.IntegerField()),
                ('engine_power', models.IntegerField()),
                ('last_tech_exam', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street_addres', models.CharField(max_length=30)),
                ('local_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pesel', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('street_addres', models.CharField(max_length=30)),
                ('loacal_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district_office.InsuranceCompany')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district_office.Person')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district_office.Person'),
        ),
    ]
