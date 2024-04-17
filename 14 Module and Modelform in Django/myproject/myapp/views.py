from django.shortcuts import render, redirect
from . import models
from myapp.forms import StudentForm
# Create your views here.

def home(request):
    # student = models.Student.objects.all()
    std  = StudentForm()
    return render (request, 'home.html',{'data':std})


def delete_student(request, roll):
    std = models.Student.objects.get(pk= roll).delete()
    return redirect('homepage')

