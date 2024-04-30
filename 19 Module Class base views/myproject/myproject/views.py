from django.shortcuts import render, get_object_or_404
from posts.models import Post
from categories.models import Category

def home(request, category_slug=None):
    data = Post.objects.all()
    categories = Category.objects.all()

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        data = Post.objects.filter(category=category)

    return render(request, 'home.html', {'data': data, 'categories': categories})
