from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import StudentRegistration

# Create your views here.

def showformdata(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')

            print('Name:', fm.cleaned_data['name'])
        
            print('Email:', fm.cleaned_data['email'])
     
            
         
            


    else:
        fm = StudentRegistration()
        print('ye get se aya hai')

    return render(request, 'enroll/enroll.html', {'form': fm})
