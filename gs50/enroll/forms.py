
from cProfile import label
from dataclasses import fields
from pyexpat import model
from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    class Meta:
        model = Student
        fields = ['name','password', 'email' ]
        labels = {'name':'Enter Name', 'password':'Enter Password', 'email':'Enter Email'}
        help_text = {'name':'Enter Your full Name'}
        error_messages = {'name':{'required':'naam likhna jaruri hai'}}
        widgets = {'password':forms.PasswordInput}

