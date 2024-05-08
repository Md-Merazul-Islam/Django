from .forms import CarForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from .models import Car, Order, Brand
# Create your views here.

# add brand name


class CreateBrand(LoginRequiredMixin, CreateView):
    model = Brand
    fields = ['name']
    template_name = 'add_brand.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, f'Brand created successfully.')
        return super().form_valid(form)



# add car
class AddCarView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self):
        return Car.objects.all()




def brand_list(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'brands': brands, 'cars':cars})