from django.views.generic import ListView, TemplateView
from .models import Book
from categories.models import Category

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context
