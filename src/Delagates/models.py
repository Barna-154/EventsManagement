from django.db import models
from datetime import datetime, date

# delagates category models
class NonPaying(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Surname = models.CharField(max_length=30, null=False)
    Organisation = models.CharField(max_length=50, null=False)
    Email = models.EmailField(max_length=254, null=False)


    def __str__(self):
        return self.Surname
    


class Paying(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Surname = models.CharField( max_length=30, null=False)
    Organisation = models.CharField( max_length=50, null=False)
    Email = models.EmailField(max_length=254, null=False)
    InvoiceNum = models.IntegerField(null=False)
    ReceiptNum = models.IntegerField(null=False)
    Amount = models.FloatField(null=True)
    payment_for = (
        ('FullBoard', 'FullBoard'),
        ('Registration', 'Registration'),
        ('Exibition', 'Exibition'),
    )
    Options = models.CharField(max_length=30, choices = payment_for, null=False)
    Payment_Date = models.DateField("Payment Date(MM/DD/YYYY)", auto_now_add=False, auto_now=False, blank=True)
    TimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank = True)

    def __str__(self):
        return self.Surname


class Sponsorship(models.Model):
    Name = models.CharField(max_length=30, null=True)
    Surname = models.CharField( max_length=30, null=True)
    Organisation = models.CharField( max_length=50, null=False)
    Email = models.EmailField(max_length=254, null=False)
    InvoiceNum = models.CharField(max_length=20, null=True)
    ReceiptNum = models.CharField(max_length=20, null=True)
    Amount = models.FloatField(null=True)
    p_choices = (
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
    )
    Packages = models.CharField(max_length=30, choices = p_choices, null=False)
    Payment_Date = models.DateField("Payment Date(MM/DD/YYYY)",auto_now_add=False, auto_now=False)
    TimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.Surname


class Exibitor(models.Model):
    Name = models.CharField(max_length=30, null=True)
    Surname = models.CharField( max_length=30, null=True)
    Organisation = models.CharField( max_length=50, null=False)
    Email = models.EmailField(max_length=254, null=False)
    InvoiceNum = models.IntegerField(null=True)
    ReceiptNum = models.IntegerField(null=True)
    Amount = models.FloatField(null=True)
    Payment_Date = models.DateField("Payment Date(MM/DD/YYYY)",auto_now_add=False, auto_now=False)
    TimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.Surname