
from django.urls import path
from . import views

urlpatterns = [


    path('about/',views.about, name="about" ),
    path('from/',views.contact_from, name="contact" ),
    path('django_form/',views.password_verification, name="django_form" ),

    
]