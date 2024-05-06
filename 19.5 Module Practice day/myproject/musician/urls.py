from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicianListViews.as_view(), name='musician_list'),
    path('create/', views.MusicianCreateView.as_view(), name='musician_create'),
    path('edit/<int:pk>/', views.MusicianUpdateViews.as_view(), name='musician_edit'),
    path('delete/<int:pk>/', views.MusicianDeleteView.as_view(), name='musician_delete'),
]