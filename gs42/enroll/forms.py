from distutils.command.upload import upload
from django.core import validators
from django import forms

class StudentRegistration(forms.Form):
    #To study built-in Validators 
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(min_length=5, max_length=50)
    
    #To study built-in 




    