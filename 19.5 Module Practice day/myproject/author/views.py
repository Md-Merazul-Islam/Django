
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, FormView
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
class RegisterView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message='Your profile was create successfully'
    
    
    
class User_login(LoginView):
    template_name = 'register.html'
    
    def form_valid(self,form):
        super.form_valid(form)
        messages.success(self.request,'Successfully Login in')
        return redirect('profile')
        
    def form_invalid(self, form):
        super().form_invalid(form)
        messages.warning(self.request,'Invalid user or password')
        return redirect('register')
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    def get_success_url(self) :
        return reverse_lazy('profile')
         
        
        
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')