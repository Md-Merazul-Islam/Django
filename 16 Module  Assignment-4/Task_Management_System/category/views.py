from django.shortcuts import render,redirect
from . models import Category
from . forms import CategoryForm
from django.contrib import messages
# Create your views here.

def show_category(request):
    categories = Category.objects.all()
    return render(request,'show_category.html',{'categories':categories})


def add_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')  # Added request argument
            return redirect('show_category')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
