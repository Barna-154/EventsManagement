# Generated by Django 3.0.6 on 2020-05-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delagates', '0004_auto_20200323_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exibitor',
            name='Payment_Date',
            field=models.DateField(verbose_name='Payment Date(MM/DD/YYYY)'),
        ),
        migrations.AlterField(
            model_name='paying',
            name='Payment_Date',
            field=models.DateField(blank=True, verbose_name='Payment Date(MM/DD/YYYY)'),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Payment_Date',
            field=models.DateField(verbose_name='Payment Date(MM/DD/YYYY)'),
        ),
    ]
