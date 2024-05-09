from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import  CreateView
from .models import  Brand
from django.contrib.messages.views import SuccessMessageMixin

class CreateBrand(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Brand
    fields = ['name']
    template_name = 'add_brand.html'
    success_url = reverse_lazy('home')
    success_message = "Brand created successfully."

    def form_valid(self, form):
        return super().form_valid(form)
