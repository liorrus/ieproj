from django.contrib.auth.models import User
from django import forms
from .models import Contact


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {'first_name', 'last_name', 'email', 'message'}
