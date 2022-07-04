from django.urls import path
from . import views

urlPatterns = [
    path('home', views.patient_home, name='patient_home'),
    path('new-appointment', views.new_appointment, name='new_appointment'),
    path('doctor/<int:doctor_id>', views.doctor_profile, name='doctor_profile'),
    path('appointment/add/<int:slot_id>', views.add_appointment, name='add_appointment'),
]