from distutils.command.upload import upload
import email
from django import forms

class StudentRegistration(forms.Form):
    #To study different field types (built-in)
    name = forms.CharField(error_messages={'required': 'Enter Your Name'} )#strip=False, min_length=5, max_length=10, empty_value="Jakir"
    roll = forms.IntegerField(min_value=5, max_value=40)
    amount = forms.DecimalField(max_digits=4, decimal_places=1)#min_value, max_value
    rate = forms.FloatField() #float means .0
    agree = forms.BooleanField(label='I Agree', label_suffix=' ', error_messages={'required': 'Tick mar bc'})
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    #website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(min_length=5, max_length=50, widget=forms.PasswordInput())
    description = forms.CharField(widget=forms.Textarea(), initial='Good')
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class': 'somecss1', 'id': 'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols':50}))

