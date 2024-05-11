from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

class UserRegistrationView(FormView):
    template_name='accounts/register_form.html'
    form_class = UserRegistrationForm
    success_url= reverse_lazy('register')
    
    def form_valid(self, form):
        user= form.save()
        login(user)
        return super().form_valid(form)
    