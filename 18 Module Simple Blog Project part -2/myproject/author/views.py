from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Successfully registered.')
            return redirect('register')  
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})

def user_Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request,'Successfully login.')
                login(request, user)
                return redirect('profile')  
            else:
                messages.warning(request,'Login information incorrect!')
                return redirect('register')  
                
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'login'}) 


def profile_view(request):
    # Implement your profile view logic here
    return render(request, 'profile.html')