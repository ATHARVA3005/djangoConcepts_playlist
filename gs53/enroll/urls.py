
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:my_id>/', views.show_details, name="details"),
    #path('student/<str:my_id>/', views.show_details, name="details"),
    path('<int:my_id>/<int:my_sid>/', views.show_sdetails, name="sdetails"),
    
]
