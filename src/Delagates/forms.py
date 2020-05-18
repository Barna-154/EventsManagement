from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

#registerion form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# user input forms 
class NonPayingForm(ModelForm):
    class Meta:
        model = NonPaying
        fields = '__all__'

class PayingForm(ModelForm):
    class Meta:
        model = Paying
        fields = '__all__'

class SponsorshipForm(ModelForm):
    class Meta:
        model = Sponsorship
        fields = '__all__'


class ExibitorForm(ModelForm):
    class Meta:
        model = Exibitor
        fields = '__all__'