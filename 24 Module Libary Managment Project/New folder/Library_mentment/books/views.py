# from .forms import BookForm
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
# from django.views.generic import ListView, CreateView
# from .models import Book,Category
# from django.contrib.messages.views import SuccessMessageMixin


# class AddBookView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
#     model = Book
#     form_class= BookForm
#     template_name = 'add_book.html'
#     success_url=reverse_lazy('home')
#     success_message ='Book added successfully'
#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class BookListView(ListView):
#     model= Book
#     template_name = 'book_list.html'
    
#     def get_queryset(self):
#         return Book.objects.all()

# def Book_list_by_category(request,category_slug=None):
#     data = Book.objects.all()
#     if category_slug is not None:
#         category = Category.objects.get(slug=category_slug)
#         data = Category.objects.filter(category=category)
#     categories = Category.objects.all()
#     return render(request, 'home.html', {'data': data, 'categories': categories})
    
    
    
# def home (request):
#     return render (request,'home.html' )


from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Book, Category

def book_list_by_category(request, category_slug=None):
    books = Book.objects.all()
    category = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(categories=category)

    categories = Category.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'categories': categories, 'category': category})






