from django.shortcuts import renderfrom 
from django.http import HttpResponse

# Create your views here.

def fees_django(request):
    return HttpResponse(300)

def fees_python(request):
    return HttpResponse(200)

