from django import forms 
from .models import LendMe

class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput)


class FinanceInfo(forms.ModelForm):
    class Meta: 
        model = LendMe
        fields = ['first_name', 'last_name', 'annual_income', 'pan_card', 'annual_income', 'credit_score']
    # first_name = forms.CharField(label='First Name', max_length=255) 
    # last_name = forms.CharField(label='Last Name', max_length=255)
    # pan_card = forms.CharField(label='PAN', max_length=255)
    # annual_income = forms.IntegerField(label='Annual Income') 
    # credit_score = forms.IntegerField(label='Credit Score') 
       
    