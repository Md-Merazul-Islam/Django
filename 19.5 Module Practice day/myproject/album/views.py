from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import  Album
from .forms import AlbumForm 

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    
class AlbumDeleteView(DeleteView):
    model =Album
    success_url = reverse_lazy('musician_list')
    template_name ='album_delete.html'