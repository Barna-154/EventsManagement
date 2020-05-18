# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exibitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Surname', models.CharField(max_length=30, null=True)),
                ('Organisation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('InvoiceNum', models.IntegerField()),
                ('ReceiptNum', models.IntegerField()),
                ('Amount', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='NonPaying',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30)),
                ('Surname', models.CharField(max_length=30)),
                ('Organisation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Paying',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30)),
                ('Surname', models.CharField(max_length=30)),
                ('Organisation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('InvoiceNum', models.IntegerField()),
                ('ReceiptNum', models.IntegerField()),
                ('Amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('Options', models.CharField(max_length=30, choices=[('FullBoard', 'FullBoard'), ('Registration', 'Registration'), ('Exibition', 'Exibition')])),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Surname', models.CharField(max_length=30, null=True)),
                ('Organisation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('InvoiceNum', models.IntegerField()),
                ('ReceiptNum', models.IntegerField()),
                ('Amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('Packages', models.CharField(max_length=30, choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')])),
            ],
        ),
    ]
