from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user.role == 'PATIENT':
                return redirect(settings.LOGIN_REDIRECT_URL)
            elif user.role == 'PROFESSIONAL':
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
          form = forms.RegisterForm()
          return render(request, 'index.html', {'form': form})
    else:
      form = forms.RegisterForm()
      return render(request, "index.html", {'form': form})
