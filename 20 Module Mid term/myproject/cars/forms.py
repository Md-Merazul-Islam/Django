from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'name', 'description', 'image', 'quantity', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter car name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
        }
