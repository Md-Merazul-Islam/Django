from django.urls import path 
from . import views

urlpatterns = [
    path('carlist/',views.CarListView.as_view(),name='car_list'),
    path('add-car/',views.AddCarView.as_view(),name='add_car'),
    path('add-brand/',views.CreateBrand.as_view(),name='add_brand'),
    path('car-list/',views.brand_list,name='car_list'),
    
]

