from . import views
from django.urls import path
from django import urls

urlpatterns = [
    path('learndj/', views.learn_django),
]
