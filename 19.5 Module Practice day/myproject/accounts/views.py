from django.contrib.auth.views import LogoutView
from typing import Any
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Successfully registered.')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    
    def form_valid(self, form):
        messages.error(self.request ,'Successfully login. ')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request ,'Invalid username or password. ')
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["type"] ='Login' 
        return context
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
        

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your password has been changed successfully.')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render (request,'home.html')