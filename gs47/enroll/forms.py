from . import views
from django.core import validators
from django import forms


class StudentRegistration(forms.Form):
    error_css_class='error'
    required_css_class='required'
    #To Study coonection of form with database in django
    name = forms.CharField(error_messages={'required': 'Enter your name'})
    email = forms.EmailField(error_messages={'required': 'Enter your Email'})
    password = forms.CharField(error_messages={'required': 'Enter your Password'})

    #To Study coonection of form with database in django





    