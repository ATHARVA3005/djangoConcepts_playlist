from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    cname = 'Mhango'
    duration = '4 months'
    seats = 10 
    django_details = {'nm': cname, 'du':duration, 'st':10}
    return render(request, 'course/courseone.html', django_details)


def learn_python(request):
    return render(request, 'course/coursetwo.html')