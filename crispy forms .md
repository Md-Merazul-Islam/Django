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
    

# [Media file](https://djangocentral.com/managing-media-files-in-django/)

  Open settings.py file of your project and add the following configuration.

        # Base url to serve media files
        MEDIA_URL = '/media/'
        
        # Path where media is stored'
        MEDIA_ROOT = BASE_DIR / 'media'

* url.py 

      from django.conf import settings
      from django.conf.urls.static import static
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          ...]
      if settings.DEBUG:
  
          urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)

  * [ImageField – Django Models](https://www.geeksforgeeks.org/imagefield-django-models/)

        pip install Pillow 

        

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
        



# BASE HTML CODE 
            
                 
              <!doctype html>
              {% load static %}
              <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Bootstrap demo</title>
                
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
              
                <link rel="stylesheet" href="{% static 'boostrap/css/all.min.css' %}">
                <link rel="stylesheet" href="{% static 'boostrap/css/bootstrap.css' %}">
                <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Satisfy&display=swap" rel="stylesheet">
                {% block corecss %}
                    <link rel="stylesheet" href="{% static 'boostrap/css/style.css' %}">
                {% endblock corecss %}
              
              
                <style>
              
              .mx-container {
                width: 100%; 
                max-width: 1680px; 
                margin: 0 auto; 
              }
              
              
              @media (max-width: 768px) {
                .mx-container {
                    max-width: 90%; 
                }
              }
              
                </style>
              
              
              
              
              </head>
              <body>
              
                <nav class=" navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
                  <div class="mx-container container-fluid">
                    <a class="navbar-brand" href="#">MVTV</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class=" collapse navbar-collapse justify-center" id="navbarSupportedContent">
                
                      <ul class="navbar-nav mx-auto me-auto mb-2 mb-lg-0">
                        
                        {% comment %} --------------authentication check {% endcomment %}
                        {% if request.user.is_authenticated %}
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="{% url 'home' %}">Home</a>
                        </li>
                        
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="{% url 'musician_list' %}">Musicina  </a>
                      
                        </li>
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="{% url 'album_list' %}">Album </a>
                        </li>
              
                        <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Create
                          </a>
                          <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="{% url 'musician_create' %}">Create Musician </a></li>
                            <li><a class="dropdown-item" href="{% url 'album_create' %}">Create Album </a></li>
                          
                          </ul>
                        </li>
              
                        {% endif %}
                      </ul>
                
                      <form class="d-flex " role="search">
                        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Search</button>
                      </form>
                
                      <div class='d-flex'>
                        <ul class="navbar-nav">
                          {% if request.user.is_authenticated %}
                          <li class="nav-item">
                            {% comment %} <a class="btn btn-warning mx-4" aria-current="page" href="{% url 'profile' %}">Profile</a> {% endcomment %}
                          </li>
                          <li class="nav-item">
                            <a class="btn btn-warning mx-4" aria-current="page" href="{% url 'user_logout' %}">Logout</a>
                          </li>
                          {% else %}
                          <li class="nav-item">
                            <a class="btn btn-warning mx-2" aria-current="page" href="{% url 'register' %}">Register</a>
                          </li>
                          <li class="nav-item">
                            <a class="btn btn-warning mx-2" aria-current="page" href="{% url 'user_login' %}">Login</a>
                          </li>
                          {% endif %}
                        </ul>
                      </div>
                
                    </div>
                  </div>
                </nav>
                
                <div class='justify-content-center d-flex align-items-center'>
                  {% for message in messages %}
                <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header">
                    {% comment %} <img src="..." class="rounded me-2" alt="..."> {% endcomment %}
                    <strong class="me-auto">Congratulations</strong>
                    <small>Now</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                  </div>
                  <div class="toast-body">
                    <small>{{ message }}</small>
                  </div>
                </div>
                {% endfor %}
                </div>
                
                
              <div class="mx-container">
              
                {% block content %}{% endblock content %}
              </div>
              
              
              
              
              
              
              
              
              <script src="{% static 'boostrap/js/jquery.js' %}"></script>
              <script src="{% static 'boostrap/js/popper.js' %}"></script>
              <script src="{% static 'boostrap/js/all.min.js' %}"></script>
              <script src="{% static 'boostrap/js/bootstrap.js' %}"></script>
              
              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
              <script>
                // Initialize Bootstrap toast
                var toastElList = [].slice.call(document.querySelectorAll('.toast'));
                var toastList = toastElList.map(function(toastEl) {
                  return new bootstrap.Toast(toastEl);
                });
              
                // Show all toasts
                toastList.forEach(function(toast) {
                  toast.show();
                });
              </script>
              </body>
              </html>


# A RESPONSIVE PAGE HTML CODE :

            {% extends "base.html" %} 
            {% block content %}
            <div class="d-flex flex-wrap row vh-100 align-items-center ">
              <div class="col-lg-8 col-md-12 pt-5 d-flex justify-content-center">
                <div class="text-center" style="width: 80%">
                  <h1 style="font-size: 80px; font-weight: bold; color: #D44DA9">
                    Welcome To Our Website
                  </h1>
                  <p class="text-left" style="color: #0D3858;">
                    Michael Walker is leading a revolution in today’s music industry. Having personally reached 17 million views on YouTube, working with Grammy Award-winning producers and touring internationally to perform for hundreds of thousands of fans worldwide - Michael is one of those rare mentors who has actually walked the walk of their own methodology.
                  </p>
                </div>
              </div>
            
              <div class="col-lg-4 col-md-12 pt-5 align-content-center justify-content-center">
                {% load static %}
                <img class="w-100" src="{% static 'banner.png' %}" alt="Example Image" />
              </div>
            </div>
            {% endblock %}

            
