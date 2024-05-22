from django import forms
from .models import Book, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'name', 'description',
                  'image', 'quantity', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter car name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')