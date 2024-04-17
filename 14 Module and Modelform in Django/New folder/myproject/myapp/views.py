from django.shortcuts import render, redirect
from myapp.forms import StudentForm
# Create your views here.

from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully!")
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})
