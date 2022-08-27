from distutils.command.upload import upload
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.HiddenInput())
    about_me = forms.IntegerField(widget=forms.Textarea())
    Are_you_18_years_old = forms.IntegerField(widget=forms.CheckboxInput())
    upload_resume = forms.CharField(widget=forms.FileInput())

    #adding class attribute in form field
    naam = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1', 'id': 'uniqueid'}))

