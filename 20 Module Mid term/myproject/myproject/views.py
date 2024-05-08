from django.shortcuts import render, get_object_or_404
from cars.models import Car
from cars.models import Brand

def home(request, category_slug=None):
    data = Car.objects.all()
    categories = Brand.objects.all()

    if category_slug is not None:
        category = get_object_or_404(Brand, slug=category_slug)
        data = Car.objects.filter(category=category)

    return render(request, 'home.html', {'data': data, 'categories': categories})