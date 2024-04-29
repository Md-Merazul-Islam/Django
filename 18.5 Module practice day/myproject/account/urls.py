
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/change-password/',views.change_password, name='forget_password' ),
    path('profile/change-password/change-password-with-previous/',views.chg_pass_with_pass, name='chg_pass_with_password'),
    path('profile/change-password/change-password-without-previous/',views.chg_pass_without_pass, name='chg_pass_without_password')
    
]


