from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm 
# from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Author
from .forms import ChangePasswordForm

def home (request):
    return render (request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Create a account successfully.')
            return redirect('user_login')
    else:
        form= forms.RegisterForm()
    return render(request,'register.html',{'form':form,'type':'register'})
            
        
def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user:
                messages.success(request,'Login successfully!')
                login(request,user)
                return redirect('home')
            else :
                messages.warning(request,'Login information is not correct!')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'login'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('user_login')
        

@login_required
def user_profile(request):
    return render(request, 'profile.html')

@login_required
def chg_pass_with_pass(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Password successfully updated!')
            return redirect('profile')
        
    else :
        form = PasswordChangeForm(request.user)
    return render(request,'change_pass.html',{'form':form})
        
@login_required
def chg_pass_without_pass(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST)
        if form.is_valid():
            new_pass = form.cleaned_data['new_pass']
            request.user.set_password(new_pass)
            request.user.save()
            messages.success(request, 'Password successfully updated!')
            return redirect('home')  
    else:
        form = CustomPasswordChangeForm()  
    return render(request, 'change_pass.html', {'form': form})

@login_required
def change_password(request):
    return render(request,'chg.html')