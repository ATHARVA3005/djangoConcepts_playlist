from distutils.command.upload import upload
import email
from django import forms

class StudentRegistration(forms.Form):
    #To study cleaning ND VALIDATING complete form IN DJANGO
    name = forms.CharField()
    email = forms.EmailField(min_length=5, max_length=50)
    
    #To study cleaning ND VALIDATING complete form IN DJANGO

    def clean(self):
        cleaned_data  = super().clean
        ()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 4:
            raise forms.ValidationError('Name should be more than equal 4')
            
        if len(valemail) < 10:
            raise forms.ValidationError('Email should be more than equal 10')



    