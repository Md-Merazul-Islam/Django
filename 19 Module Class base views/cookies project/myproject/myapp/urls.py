
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home, name='home'),
    path('get/',views.get_cookie, name='get_cookie'),
    path('delete-cookie/',views.del_cookie, name='get_cookie'),
    path('get_session/',views.get_session, name='get_session'),
    path('set_session/',views.set_session, name='set_session'),
    path('del_session/',views.delete_session, name='_session'),
]
