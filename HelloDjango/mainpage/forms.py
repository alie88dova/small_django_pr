from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *



class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Name',
                                                                       'class': "register-input"}),)
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Email',
                                                                       'class': "register-input"}),)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'password',
                                                                       'class': "register-input"}),)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Repeate password',
                                                                       'class': "register-input"}),)


    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={'placeholder':'Name'}),
            "email": forms.TextInput(attrs={'placeholder':'Email'}),
            "password1": forms.PasswordInput(attrs={'placeholder':'Password'}),
            "password2": forms.PasswordInput(attrs={'placeholder': 'Repeat password'}),
        }

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Name',
                                                                       'class': "register-input"}),)

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password',
                                                                            'class': "register-input"}), )


    class Meta:
        model = User
        fields = ('username', "password")
        widgets = {
            "username": forms.TextInput(attrs={'placeholder':'Name'}),
            "password": forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }