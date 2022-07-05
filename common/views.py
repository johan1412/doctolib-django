import datetime
from django.shortcuts import render, redirect
from common.forms import EditDoctorForm, FilterDoctorsForm, SlotForm

from common.models import Appointment, Slot
from register.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    # get the next appointments for the patient
    if request.user.is_authenticated:
      if request.user.role == 'PATIENT':
        appointments = Appointment.objects.filter(patient=request.user)
        # get next appointments grather than current time
        next_appointments = appointments.filter(slot__date__gte=datetime.datetime.now())
        next_appointments = next_appointments.order_by('slot.date')
        # get doctors related to the patient
        doctors = []
        for appointment in appointments:
            doctors.append(appointment.doctor)
        doctors = list(dict.fromkeys(doctors))
      else:
        return render(request, 'common/pro_home.html')
    else:
      next_appointments = []
      doctors = []

    return render(request, 'common/patient_home.html', { "appointments" : next_appointments, "doctors" : doctors })

def new_appointment(request):
    if request.method == 'POST':
      form = FilterDoctorsForm(request.POST)
      if form.is_valid():
        # get the doctors for the selected city and speciality
        doctors = User.objects.filter(city=form.cleaned_data['city'], speciality=form.cleaned_data['speciality'])
        new_form = FilterDoctorsForm()

        return render(request, 'common/new_appointment.html', { "form" : new_form, "doctors" : doctors })
      else:
        form = FilterDoctorsForm()
        doctors = User.objects.filter(role='Pro')
        return render(request, 'common/new_appointment.html', { "form" : form , "doctors" : doctors })
    else:
      form = FilterDoctorsForm()
      doctors = User.objects.filter(role='Pro')

      return render(request, 'common/new_appointment.html', { "form" : form, "doctors" : doctors })

def doctor_profile(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
    return render(request, 'common/doctor_profile.html', { "doctor" : doctor, "slots" : slots })

def add_appointment(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if slot.is_reserved:
      doctor = slot.doctor
      slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
      return render(request, 'common/doctor_profile.html', { "error" : "Désolé, ce créneau est déjà pris", "doctor" : doctor, "slots" : slots })
    else:
      slot.is_reserved = True
      slot.save()
      appointment = Appointment(doctor=slot.doctor, patient=request.user, slot=slot)
      appointment.save()
      doctor = slot.doctor
      slots = Slot.objects.filter(doctor=doctor).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
      return render(request, 'common/doctor_profile.html', { "success" : "Votre rendez-vous a été enregistré", "doctor" : doctor, "slots" : slots })

def doctor_edit(request):
    if request.method == 'POST':
      form = EditDoctorForm(request.POST)
      if form.is_valid():
        doctor = User.objects.get(id=request.user.id)
        doctor.description = form.cleaned_data['description']
        doctor.save()
        new_form = EditDoctorForm()
        return render(request, 'common/doctor_edit.html', { "success" : "Votre profil a été mis à jour", "form" : new_form })
      else:
        new_form = EditDoctorForm()
        return render(request, 'common/doctor_edit.html', { "error" : "Veuillez corriger les erreurs", "form" : new_form })
    else:
      form = EditDoctorForm()
      return render(request, 'common/doctor_edit.html', { "form" : form })

@login_required
def doctor_agenda(request):
    if request.method == 'POST':
      form = SlotForm(request.POST)
      if form.is_valid():
        doctor = User.objects.get(id=request.user.id)
        slot = Slot(doctor=doctor, date=form.cleaned_data['date'], start_time=form.cleaned_data['start_time'], end_time=form.cleaned_data['end_time'])
        slot.save()
        new_form = SlotForm()
        slots = Slot.objects.filter(doctor=request.user).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
        return render(request, 'common/doctor_agenda.html', { "success" : "Votre créneau a été ajouté", "form" : new_form, "slots" : slots })
      else:
        new_form = SlotForm()
        slots = Slot.objects.filter(doctor=request.user).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
        return render(request, 'common/doctor_agenda.html', { "error" : "Veuillez corriger les erreurs", "form" : new_form, "slots" : slots })
    else:
      form = SlotForm()
      slots = Slot.objects.filter(doctor=request.user).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
      return render(request, 'common/doctor_agenda.html', { "slots" : slots, "form" : form })

@login_required
def delete_creneau(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    slot.delete()
    slots = Slot.objects.filter(doctor=request.user).filter(date__gt=datetime.datetime.now()).order_by('date').order_by('start_time')
    return render(request, 'common/doctor_agenda.html', { "success" : "Votre créneau a été supprimé", "slots" : slots })

@login_required
def my_profile(request):
    if request.user.role == 'PATIENT':
      return redirect('/')
    else:
      return render(request, 'common/pro_profile.html')