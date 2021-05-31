from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['account_name', 'username', 'password', 'website']
        labels = {'account_name': 'Account Name', 'username': 'Username', 'password': 'Password', 'website': 'Website'}
        widgets = {'account_name': forms.TextInput(attrs={'style': 'font-size: 40px'}),}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']