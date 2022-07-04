from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if not request.user.is_anonymous:
        return redirect("account_client" if request.user.role == 'PATIENT' else "account_pro")

    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user.role == 'PATIENT':
                return redirect(settings.LOGIN_REDIRECT_URL + '/patient')
            elif user.role == 'PROFESSIONAL':
                return redirect(settings.LOGIN_REDIRECT_URL + '/pro')
    return render(request, "register/index.html", context={'form': form})
