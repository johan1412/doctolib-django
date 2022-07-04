import datetime
from django.shortcuts import render
from core.forms import FilterDoctorsForm

from core.models import Appointment, Slot
from django.contrib.auth.models import User

# Create your views here.

def patient_home(request):

    # get the next appointments for the patient
    appointments = Appointment.objects.filter(patient=request.user)
    next_appointments = appointments.filter(date__gt=datetime.now())
    next_appointments = next_appointments.order_by('date')
    # get doctors related to the patient
    doctors = []
    for appointment in appointments:
        doctors.append(appointment.doctor)
    doctors = list(dict.fromkeys(doctors))

    return render(request, 'core/patient_home.html', { "appointments" : next_appointments, "doctors" : doctors })

def new_appointment(request):
    if request.method == 'POST':
      form = FilterDoctorsForm(request.POST)
      if form.is_valid():
        # get the doctors for the selected city and speciality
        doctors = User.objects.filter(city=form.cleaned_data['city'], speciality=form.cleaned_data['speciality'])
        new_form = FilterDoctorsForm()

        return render(request, 'core/new_appointment.html', { "form" : new_form, "doctors" : doctors })
    else:
      form = FilterDoctorsForm()
      doctors = User.objects.filter(role='Pro')

      return render(request, 'core/new_appointment.html', { "form" : form, "doctors" : doctors })

def doctor_profile(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.now()).order_by('date').order_by('start_time')
    return render(request, 'core/doctor_profile.html', { "doctor" : doctor, "slots" : slots })

def add_appointment(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if slot.is_reserved:
      doctor = slot.doctor
      slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.now()).order_by('date').order_by('start_time')
      return render(request, 'core/doctor_profile.html', { "error" : "Désolé, ce créneau est déjà pris", "doctor" : doctor, "slots" : slots })
    else:
      slot.is_reserved = True
      slot.save()
      appointment = Appointment(doctor=slot.doctor, patient=request.user, slot=slot)
      appointment.save()
      doctor = slot.doctor
      slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.now()).order_by('date').order_by('start_time')
      return render(request, 'core/doctor_profile.html', { "success" : "Votre rendez-vous a été enregistré", "doctor" : doctor, "slots" : slots })