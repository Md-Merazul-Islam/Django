from django import forms
from datetime import datetime

class contactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
    age = forms.IntegerField()
    birthday = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    choices = [('B','Black'),('G','Green'),('Y','Yellow')]
    favorite_color = forms.ChoiceField(choices=choices)
    most_favorite_colorfv = forms.ChoiceField(widget=forms.RadioSelect,choices=choices)
    musltipale_favorite_color= forms.MultipleChoiceField(choices=choices)
    message = forms.CharField(label="Your Message", widget=forms.Textarea)
    agree = forms.BooleanField() 
