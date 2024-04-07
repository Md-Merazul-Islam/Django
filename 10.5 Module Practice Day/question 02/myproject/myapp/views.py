from django.shortcuts import render

# Create your views here.

def about(request):
    return render (request,'myapp/about.html')

def contact(request):
    return render (request,'myapp/contact.html')

def help(request):
    return render (request,'myapp/help.html')
