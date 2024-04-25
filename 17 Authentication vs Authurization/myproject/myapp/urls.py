
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='home'),
    path('signup/',views.SignUp, name ='signup'),
    path('login/',views.user_login, name ='login'),
    path('logout/',views.user_logout, name ='logout'),
    path('passchange/',views.pass_change, name ='passchange'),
    path('passchange2/',views.pass_change2, name ='passchange2'),
    path('profile/',views.profile, name ='profile'),
    
]
