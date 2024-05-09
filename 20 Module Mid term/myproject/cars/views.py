from .forms import CarForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from .models import Car
from brand.models import Brand
from django.contrib.messages.views import SuccessMessageMixin

# add car
class AddCarView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('home')
    success_message = "Car was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self):
        return Car.objects.all()




# def car_list_by_brand(request, brand_slug=None):
#     brands = Brand.objects.all()
#     cars = Car.objects.all()

#     if brand_slug is not None:
#         brand = get_object_or_404(Brand, slug=brand_slug)
#         cars = cars.objects.filter(brand=brand)
    
#     return render(request, 'car_list.html', {'brands': brands, 'cars': cars})


def car_list_by_brand(request):
    cars = None
    brands = Brand.objects.all()
    brand_id = request.GET.get('brand')  
    if brand_id:
        cars = Car.get_all_cars_by_id(brand_id)
    else:
        cars = Car.get_all_cars()
    data = {
        'cars': cars,
        'brands': brands
    }
    return render(request, 'car_list.html', data)

