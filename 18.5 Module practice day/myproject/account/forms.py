from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name' ,'email',  ]


class CustomPasswordChangeForm(forms.Form):
    new_pass = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_pass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()  
        new_pass = cleaned_data.get('new_pass')
        confirm_pass = cleaned_data.get('confirm_pass')

        if new_pass != confirm_pass:
            raise forms.ValidationError("New password and confirm password must match.")
        
        return cleaned_data
