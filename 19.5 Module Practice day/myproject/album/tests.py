from django.urls import path
from .views import *

urlpatterns = [
    path('create/',AlbumCreateView.as_view(),name='album_create'),
    path('update/<int:pk>',AlbumDeleteView.as_view(),name='musician_delete'),
    path('delete/<int:pk>',AlbumUpdateView.as_view(),name='musician_update'),
   
]