from . import views
from django.core import validators
from django import forms


class StudentRegistration(forms.Form):
    #To Study styling form errors
    name = forms.CharField(error_messages={'required': 'Enter your name'})
    email = forms.EmailField(error_messages={'required': 'Enter your Email'}, min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': 'Enter your Password'}, min_length=5, max_length=50)

    #To Study styling form errors





    