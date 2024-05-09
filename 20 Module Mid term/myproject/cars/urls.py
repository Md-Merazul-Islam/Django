from django.urls import path
from . import views

urlpatterns = [
    path('carlist/', views.CarListView.as_view(), name='car_list'),
    path('add-car/', views.AddCarView.as_view(), name='add_car'),
    path('car-list/', views.car_list_by_brand, name='car_list'),
    path('car-list/<slug:brand_slug>', views.car_list_by_brand, name='brand_list_detail'),

]
