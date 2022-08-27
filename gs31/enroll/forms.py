from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Atharva", help_text="you can write only upto 30 characters only")
    email = forms.EmailField()
