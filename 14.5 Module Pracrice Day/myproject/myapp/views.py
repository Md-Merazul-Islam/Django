from django.shortcuts import render
from .forms import contactForm

# Create your views here.


def DjangoForm(request):
    if request.method =='POST':
        form = contactForm (request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form= contactForm()  # for blank form show
            return render(request, 'log_form.html',{'form': form, 'data': form.cleaned_data})
    else :
        form = contactForm()
    return render(request,'log_form.html',{'form':form})        