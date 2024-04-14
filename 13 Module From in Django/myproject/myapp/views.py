from django.shortcuts import render
from .forms import contactForm,StudentForms,PasswordValidationForm
# Create your views here.


def about(request):
    print(request.POST)
    if request.method == 'POST':
        em = request.POST.get('email')
        pas = request.POST.get('password')
        sel = request.POST.get('select')
        return render(request, 'myapp/about.html', {'em': em, 'pas': pas, 'sel': sel})
    else:
        return render(request, 'myapp/about.html')


def contact_from(request):
    # print(request.POST)
    if request.method == 'POST':
        em = request.POST.get('email')
        pas = request.POST.get('password')
        return render(request, 'myapp/from.html', {'em': em, 'pas': pas})
    else:
        return render(request, 'myapp/from.html')


import os
from django.conf import settings

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # upload_dir = os.path.join(settings.BASE_DIR, 'myapp/uploads/')
            # # os.makedirs(upload_dir, exist_ok=True)  # Creates the directory if it doesn't exist
            # with open(os.path.join(upload_dir, file.name), 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'myapp/django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'myapp/django_form.html', {'form': form})


# views.py
def student_forms_view(request):
    if request.method == 'POST':
        form = StudentForms(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentForms()
    return render(request, 'myapp/StudentForms.html', {'form': form})

def password_verification(request):
    if request.method == 'POST':
        form = PasswordValidationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationForm()
    return render(request, 'myapp/StudentForms.html', {'form': form})
