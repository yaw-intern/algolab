from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import customUser
import datetime

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-full-width'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-full-width'})) 
    dateOfBirth = forms.DateField(required=True, 
        widget=forms.DateInput(attrs={
            'placeholder':'Birth Date', 
            'class': 'form-control',
            'type': 'date',                                                                 
        }))
   
    class Meta:
        model = customUser
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'dateOfBirth']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-full-width'}))