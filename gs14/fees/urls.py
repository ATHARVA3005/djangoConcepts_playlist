from django import urls
from django.urls import path
from . import  views

urlpatterns = [
    path('learnpy/', views.learn_python),
]

