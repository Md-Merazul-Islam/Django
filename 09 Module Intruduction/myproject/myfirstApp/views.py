from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is home / first app page bro")

def course(request):
    return HttpResponse("Hello this is out first course")

def about(request):
    return HttpResponse("This is about section!")
