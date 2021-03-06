# Generated by Django 2.0.1 on 2018-01-29 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('police_office', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='insurance_company',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='person',
        ),
        migrations.RemoveField(
            model_name='technicalexamination',
            name='person',
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.Person'),
        ),
        migrations.AlterField(
            model_name='car',
            name='special_treatment',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='InsuranceCompany',
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
        migrations.DeleteModel(
            name='TechnicalExamination',
        ),
    ]
