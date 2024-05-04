from django.urls import path
from .views import *

urlpatterns = [
    path('create/',MusicianCreateView.as_view(),name='musician_create'),
    path('update/<int:pk>',MusicianUpdateView.as_view(),name='musician_update'),
    path('delete/<int:pk>',MusicianDeleteView.as_view(),name='musician_delete'),
    path('musician-details/<int:pk>',MusicianDetailView.as_view(),name='musician_detail'),
    
]