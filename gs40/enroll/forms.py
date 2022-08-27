from distutils.command.upload import upload
import email
from django import forms

class StudentRegistration(forms.Form):
    #To study cleaning ND VALIDATING SPECIFIC FORM FIELD IN DJANGO
    name = forms.CharField()
    email = forms.EmailField(min_length=5, max_length=50)
    password = forms.CharField(min_length=5, max_length=50, widget=forms.PasswordInput())

    #To study cleaning ND VALIDATING SPECIFIC FORM FIELD IN DJANGO

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.forms.ValidationError('Enter more than or equal to 4 character')
        return valname
    