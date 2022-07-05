from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    roles = (
        ('PROFESSIONAL', 'Practicien'),
        ('PATIENT', 'Patient')
    )

    username = forms.CharField(max_length=63, label='Nom d’utilisateur', widget=forms.TextInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    email = forms.EmailField(max_length=254, label='Adresse email', widget=forms.EmailInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    first_name = forms.CharField(max_length=63, label='Prénom', widget=forms.TextInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    last_name = forms.CharField(max_length=63, label='Nom', widget=forms.TextInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    role = forms.ChoiceField(choices=roles, label='Rôle', widget=forms.Select(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    password1 = forms.CharField(max_length=63, label='Mot de passe', widget=forms.PasswordInput(
        attrs={'class': 'shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3'}
    ))
    password2 = forms.CharField(max_length=63, label='Mot de passe', widget=forms.PasswordInput(
        attrs={'class': 'shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3'}
    ))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')
