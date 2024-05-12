from django import forms 
from .constants import GENDER_TYPE ,ACCOUNT_TYPE
from django.contrib.auth.models import User 
from .models import UserAddress,UserBankAccount
from django.contrib.auth.forms import UserCreationForm  


class UserRegistrationForm(UserCreationForm):
    birth_day = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField( choices=GENDER_TYPE)
    account_type = forms.ChoiceField( choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=120)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','account_type','birth_day','gender', 'street_address','postal_code','city','country']
        
    def save(self,commit=True):
        cur_user = super().save(commit=False)   
        if commit:
            cur_user.save()
            account_type= self.cleaned_data.get('account_type')
            gender= self.cleaned_data.get('gender')
            postal_code= self.cleaned_data.get('postal_code')
            country= self.cleaned_data.get('country')
            birth_day= self.cleaned_data.get('birth_day')
            city= self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            
            
            UserAddress.objects.create(
                user = cur_user,
                country= country,
                city=city,
                street_address=street_address,
                postal_code= postal_code,
                
            )
            
            UserBankAccount.objects.create(
                user = cur_user,
                account_type=account_type,
                gender=gender,
                birth_day=birth_day,
                account_no = 100000+ cur_user.id
                
            )
        return cur_user