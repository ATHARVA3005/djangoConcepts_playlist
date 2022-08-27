from . import views
from django.core import validators
from django import forms


class StudentRegistration(forms.Form):
    #To Study form Validators : Match two fields (Match Password and Re-enter Password)s
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label= 'Password(again)' ,widget=forms.PasswordInput)
    
    #To Study form Validators : Match two fields (Match Password and Re-enter Password)s

    def clean(self):
        cleaned_data = super().clean() 
        valpwd = cleaned_data['password']
        valrpwd = cleaned_data['rpassword']
        if valrpwd != valpwd :
            raise forms.ValidationError('Password Not Matched')




    