from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration 


# Create your views here.

def showformdata(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(id=1, name=nm, email=em, password=pw)
            reg.save()
            
        


    else:
        fm = StudentRegistration()
        print('ye get se aya hai')

    return render(request, 'enroll/enroll.html', {'form': fm})
