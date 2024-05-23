from django.shortcuts import render, redirect, get_object_or_404
from books import models ,forms
from books.models import Book ,Purchase,Category
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from books.models import Purchase
from django.views.generic import DetailView
def home(request, category_slug=None):
    books = Book.objects.all()

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(categories=category)

    categories = Category.objects.all()
    return render(request, 'home.html', {'books': books, 'categories': categories})



class DetailPostView(DetailView):
    model = models.Book
    form_class = forms.BookForm
    pk_url_kwarg = 'id'
    template_name = 'book_detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = forms.ReviewForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post  
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.ReviewForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def Borrow_Book(request,book_id):
    book = get_object_or_404(Book, pk=book_id) 
    if request.method =='POST':
        purchase = Purchase(user =request.user,book=book)
        purchase.save()
        book.quantity -=1
        book.save()
        return redirect('car_detail', id=book_id)  
    return redirect('car_detail', id=book_id)