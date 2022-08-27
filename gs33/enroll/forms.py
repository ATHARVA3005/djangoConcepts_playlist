from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile =forms.IntegerField()
    key =  forms.IntegerField(widget=forms.HiddenInput())
