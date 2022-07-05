from django.urls import path
from . import views

urlpatterns = [
    path('home', views.patient_home, name='patient_home'),
    path('new-appointment', views.new_appointment, name='new_appointment'),
]
