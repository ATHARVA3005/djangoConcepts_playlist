from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('HomePage')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse(' <h1> Hello Python </h1> ')

def learn_var(request):
    a = '<h1> Hello Variable </h1>'
    return HttpResponse(a)

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_syntax(request):
    a = 'atharvaWarokar'
    return HttpResponse(a)            


