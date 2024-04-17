
from django.urls import path
from . import views

urlpatterns = [


    path('loging/', views.DjangoForm , name ='log'),
    

]
