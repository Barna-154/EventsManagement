# Generated by Django 3.0.4 on 2020-03-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delagates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exibitor',
            name='Amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='paying',
            name='Amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Amount',
            field=models.FloatField(null=True),
        ),
    ]