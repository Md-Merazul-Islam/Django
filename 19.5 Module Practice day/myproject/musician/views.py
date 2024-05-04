from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import  Musician
from .forms import MusicianForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    
class MusicianDetailView(DetailView):
    model= Musician
    template_name ='musician_detail.html'
    
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name='musician_form.html'

class MusicianDeleteView(DeleteView):
    model = Musician
    success_url = reverse_lazy('musician_list')
    template_name= 'musician_delete.html'