import django_filters
from django_filters import CharFilter
from .models import *


class NonPayingFilter(django_filters.FilterSet):
    Surname = CharFilter(field_name='Surname', lookup_expr='icontains')
    Organisation = CharFilter(field_name='Organisation', lookup_expr='icontains')
    class Meta:
        model = NonPaying
        fields = '__all__'
        exclude = ['Name','Email']
        

class PayingFilter(django_filters.FilterSet):
    Options = CharFilter(field_name='Options', lookup_expr='icontains')
    InvoiceNum = CharFilter(field_name='InvoiceNum', lookup_expr='icontains')
    ReceiptNum = CharFilter(field_name='ReceiptNum', lookup_expr='icontains')
    class Meta:
        model = Paying
        fields = ['Options','InvoiceNum','ReceiptNum']
        

class SponsorshipFilter(django_filters.FilterSet):
    Surname = CharFilter(field_name='Surname', lookup_expr='icontains')
    InvoiceNum = CharFilter(field_name='InvoiceNum', lookup_expr='icontains')
    ReceiptNum = CharFilter(field_name='ReceiptNum', lookup_expr='icontains')
    class Meta:
        model = Sponsorship
        fields = ['Surname','InvoiceNum','ReceiptNum']

class ExibitorFilter(django_filters.FilterSet):
    Surname = CharFilter(field_name='Surname', lookup_expr='icontains')
    InvoiceNum = CharFilter(field_name='InvoiceNum', lookup_expr='icontains')
    ReceiptNum = CharFilter(field_name='ReceiptNum', lookup_expr='icontains')
    class Meta:
        model = Exibitor
        fields = ['Surname','InvoiceNum','ReceiptNum']
