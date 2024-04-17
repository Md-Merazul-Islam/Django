from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = '__all__'
        labels={
            'name': 'Student Name',
            'roll':'Student Roll'
        }
        widgets={
            'name': forms.TextInput(attrs={'class': 'btn-primary'}),
            'roll': forms.PasswordInput()
        }