from django import forms
from register.models import User


class FilterDoctorsForm(forms.Form):
    all_cities = []
    all_specialities = []
    for doctor in User.objects.filter(role='Pro'):
      if doctor.city not in all_cities:
        all_cities.append(doctor.city)
      if doctor.speciality not in all_specialities:
        all_specialities.append(doctor.speciality)
        
    city = forms.ChoiceField(choices=zip(all_cities, all_cities))
    speciality = forms.ChoiceField(choices=zip(all_specialities, all_specialities))

class EditDoctorForm(forms.Form):
    description = forms.CharField(max_length=1000, required=True)

class SlotForm(forms.Form):
    start_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class EditDoctorProfileForm(forms.Form):
    description = forms.CharField(max_length=1000)
    city = forms.CharField(max_length=100)
    speciality = forms.CharField(max_length=100)
    addressCabinet = forms.CharField(max_length=255)