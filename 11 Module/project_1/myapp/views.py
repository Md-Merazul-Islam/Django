from django.shortcuts import render

# Create your views here.

def about(request):
    return render (request,'html/about.html')

def contact(request):
    return render(request,'html/contact.html')

def home_app(request):
    return render(request,'html/app_home.html')