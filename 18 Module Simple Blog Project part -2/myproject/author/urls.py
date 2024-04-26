from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.user_Login, name='user_login'),  # Corrected the URL name to user_login
     path('profile/', views.profile_view, name='profile'),  # Corrected the URL name to user_login
]
