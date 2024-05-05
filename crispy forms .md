# Install this plugin using pip:
  
    
    pip install crispy-bootstrap5
    


# Usage
You will need to update your project's settings file to add crispy_forms and crispy_bootstrap5 to your projects INSTALLED_APPS. Also set bootstrap5 as and allowed template pack and as the default template pack for your project


INSTALLED_APPS = (

          ...
          
          "crispy_forms",
          
          "crispy_bootstrap5",
          
          ...
    
)
# add also 

          CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
      
          CRISPY_TEMPLATE_PACK = "bootstrap5"


# Html forms 

          {% extends "base.html" %}
      
          {% block content %}
          {% load crispy_forms_tags %}
          <h1 class='text-center'> Add profile page  page</h1>
      
          <div style="width: 50%; margin: auto;">
          <form action="" method="POST">
              {% csrf_token %}
              {{ form | crispy }}
              <button class="btn btn-warning">Submit</button>
          </form>
          </div>
          {% endblock %}


# static file : 

        import os
        
    
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
        ]
    
      
        

# REGISTER.html
          {% extends "base.html" %}
      
          {% block content %}
          {% load crispy_forms_tags %}
          <h1 class='text-center'>{{ type }} page</h1>
          <div style="width: 50%; margin: auto;">
          <form action="" method="POST">
              {% csrf_token %}
           <!-- {{form | crispy}}-->   
              {% for field in form %}
                  <div class="form-group">
                      {{ field.label_tag }}
                      {{ field }}
                      {% for error in field.errors %}
                          <p class="text-danger">{{ error }}</p>
                      {% endfor %}
                  </div>
              {% endfor %}
              <button type="submit" class="btn btn-warning">Submit</button>
          </form>
          </div>
          {% endblock %}





# Models.py :
        
        from django.db import models
        
        # Create your models here.
        class Author (models.Model):
            name = models.CharField(max_length=100)
            bio= models.TextField()
            phone_no = models.CharField(max_length=12)
            
            def __str__(self):
                return self.name
    

# Forms.py 
          from django import forms
          from .models import Author
          from django.contrib.auth.models import User 
          from django.contrib.auth.forms import UserCreationForm,UserChangeForm
          
          
          
          class RegistrationForm(UserCreationForm):
              first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
              # last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
          
              class Meta:
                  model = User
                  fields = ['username','first_name','last_name','email']
                  
          class ChangeUserData(UserChangeForm):
              password=None
              class Meta:
                  model = User
                  fields = ['username','first_name','last_name','email']


# adim.py 

          from django.contrib import admin
          from . import models
          
          # Register your models here.
          admin.site.register(models.Author)



# singing, login, logout ->
             
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
        
        
        #user login using class base view
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
        

#Urls.py :

        from django.urls import path
        from . import views
        
        urlpatterns = [
            
            path('', views.home, name='home'),
            path('register/', views.register, name='register'),
            path('login/', views.UserLoginView.as_view(), name='user_login'), 
            path('logout/', views.user_logout, name='user_logout'), 
            path('profile/', views.profile_view, name='profile'), 
            path('profile/edit/change_password/', views.pass_change, name='user_pass'),  
        ]
        





            
