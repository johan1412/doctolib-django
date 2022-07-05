from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new-appointment', views.new_appointment, name='new_appointment'),
    path('doctor/<int:doctor_id>', views.doctor_profile, name='doctor_profile'),
    path('doctor/profile', views.my_profile, name='my_profile'),
    path('appointment/add/<int:slot_id>', views.add_appointment, name='add_appointment'),
    path('doctor/edit', views.doctor_edit, name='doctor_edit'),
    path('doctor/agenda', views.doctor_agenda, name='doctor_agenda'),
    path('doctor/agenda/delete/<int:slot_id>', views.delete_creneau, name='delete_creneau'),
]
