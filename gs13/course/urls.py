from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learntg/', views.learn_tags),
    path('learnfp/', views.learn_loops),
    path('learncp/',views.learn_complx ),

]