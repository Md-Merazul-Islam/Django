from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='user_login'),
    path('logout/',views.LogoutView.as_view(),name='user_logout'),
    

]
