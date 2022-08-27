import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration 


# Create your views here.

def showformdata(request):

    if request.method == 'POST':
        pi = Student.objects.get(pk=1)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            #nm = fm.cleaned_data['name']
            #em = fm.cleaned_data['email']
            #pw = fm.cleaned_data['password']
            fm.save()
            #reg = Student(id=1, name=nm, email=em, password=pw)
            #reg.save()
            #reg = Student(id=1)
            #reg.delete()


    else:
        fm = StudentRegistration()
        print('ye get se aya hai')

    return render(request, 'enroll/enroll.html', {'form': fm})
