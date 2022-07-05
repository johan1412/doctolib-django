import datetime
from django.shortcuts import render
from common.forms import FilterDoctorsForm

from common.models import Appointment, Slot
from register.models import User


# Create your views here.

def home(request):

    # get the next appointments for the patient
    if request.user.is_authenticated:
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