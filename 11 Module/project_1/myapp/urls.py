
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.home_app , name ='home_app'),
    path('contact/',views.contact,name = "contact"),
    path('about/',views.about, name='about'),
    
    
]
