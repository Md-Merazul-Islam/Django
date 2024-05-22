from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Book
from categories.models import Category
from django.contrib.messages.views import SuccessMessageMixin

# add Book
class AddBookView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_Book.html'
    success_url = reverse_lazy('home')
    success_message = "Book was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookListView(ListView):
    model = Book
    template_name = 'Book_list.html'

    def get_queryset(self):
        return Book.objects.all()




def Book_list_by_Category(request, category_slug=None):
    data = Book.objects.all()

    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Book.objects.filter(category=category )
    categories = Category.objects.all()

    return render(request, 'home.html', {'data': data, 'categories': categories})
