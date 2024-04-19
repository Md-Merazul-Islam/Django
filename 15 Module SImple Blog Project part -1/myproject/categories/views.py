from django.shortcuts import render,redirect

from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST': # user post rqst korche 
        catagories_form  = forms.CetagoryForm(request.POST) # user er data capture krlam
        if catagories_form .is_valid(): #post kora data gula valid kina check koro
            catagories_form .save()
            return redirect('add_category')
    else:
        catagories_form  = forms.CetagoryForm()
    return render (request,'add_cetagories.html',{'form':catagories_form })   