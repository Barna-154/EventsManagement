from django.contrib import admin
from .models import *
from .forms import *

# form with filters and search to be outputed on the admin panel to add and remove delagates
class NonPayingAdmin(admin.ModelAdmin):
    list_display = ['Name','Surname','Organisation']
    form = NonPayingForm
    list_filter = ['Surname','Organisation',]
    search_fields = ['Surname','InvoiceNum']

class PayingAdmin(admin.ModelAdmin):
    list_display = ['Name','Surname','Organisation','Payment_Date','TimeStamp']
    form = PayingForm
    list_filter = ['Surname','Organisation','InvoiceNum','ReceiptNum']
    search_fields = ['Surname','InvoiceNum']

class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ['Surname','Organisation','InvoiceNum','ReceiptNum','Packages','Payment_Date','TimeStamp']
    form = SponsorshipForm
    list_filter = ['Surname','Organisation','InvoiceNum','ReceiptNum','Packages']
    search_fields = ['Surname','InvoiceNum']

class ExibitorAdmin(admin.ModelAdmin):
    list_display = ['Name','Surname','Organisation','InvoiceNum','ReceiptNum','Payment_Date','TimeStamp']
    form = ExibitorForm
    list_filter = ['Name','InvoiceNum','ReceiptNum']
    search_fields = ['Surname','InvoiceNum']

#directors to edit delagates using the admin panel
admin.site.register(NonPaying, NonPayingAdmin)
admin.site.register(Paying, PayingAdmin)
admin.site.register(Sponsorship, SponsorshipAdmin)
admin.site.register(Exibitor, ExibitorAdmin)