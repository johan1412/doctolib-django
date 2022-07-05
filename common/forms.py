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