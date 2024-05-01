from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_Login, name='user_login'), 
    path('login/', views.UserLoginView.as_view(), name='user_login'), 
    path('profile/', views.profile_view, name='profile'),  
    path('logout/', views.user_logout, name='user_logout'), 
    # path('logout/', views.LogoutView.as_view(), name='user_logout'), 
    path('profile/edit/change_password/', views.pass_change, name='user_pass'),  
    path('profile/edit/', views.edit_profile, name='edit_profile'),  
    # path('profile/delete/', views.delete_profile, name='delete_profile'),  
]
