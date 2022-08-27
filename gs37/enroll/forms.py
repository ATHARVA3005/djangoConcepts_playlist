from distutils.command.upload import upload
import email
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=
    forms.PasswordInput)

