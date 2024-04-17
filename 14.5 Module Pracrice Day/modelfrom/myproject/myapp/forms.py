from django import forms
from myapp.models import Student


class StudentForm (forms.ModelForm):
    class Meta : 
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Student Name ',
            'roll': 'Student Roll'
        }
        widgets = {
            'name ': forms.TextInput,
            'date_time':forms.NumberInput(attrs={'type':'date'}),
            'duration_field':forms.NumberInput(attrs={'min':'0'}),
            'ip_address': forms.RegexField(label='IP Address', regex=r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'),
          
            
        }
        help_texts = {
            'name': 'Write your full name'
        }
        error_messages={
            'name': {'required': 'Your name is required'},
      
        } 
        