from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

from . import models


def home(request):
    student = models.Student.objects.all()
    return render(request, 'home.html', {'data': student})
def add_student(request):
    if request.method =='POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
        form = forms.StudentForm()
        return render(request,'add_student.html',{'form': form})
    else :
        form = forms.StudentForm()
    return render(request,'add_student.html',{'form': form})