from django import forms

from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='Enter your name :', initial='Full Name', help_text='total length must be withing 70 character',
                           required=False,  widget=forms.Textarea(attrs={'placeholder': 'Enter your comment', 'id': 'commnetArea', 'class': 'class1 class2'}))

    # email = forms.EmailField(label='Enter you email : ')
    age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES,  widget=forms.RadioSelect)
    MEAL = [('C', 'Chicken'), ('M', 'Meat'), ('S', 'Salad')]
    cook = forms.MultipleChoiceField(
        choices=MEAL, widget=forms.CheckboxSelectMultiple)

    # file = forms.FileField()


# class StudentForms(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Name must be at least 10 characters')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Email must be .com')
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Name must be at least 10 characters')

#         if '.com' not in valemail:
#             raise forms.ValidationError('Email must be .com')


class StudentForms(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message='Enter a name with at least 10 character ')])
    email = forms.CharField(widget=forms.EmailInput, validators=[
                            validators.EmailValidator(message='Enter a valid email')])

    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(
        30, message='age maximum 40'), validators.MinValueValidator(24, message='age at least 10 age')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(
        ['png'], message='only allow png fomate photo')])

from django import forms
from django.core import validators

class PasswordValidationForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message='Enter a name with at least 10 characters ')])
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pas = cleaned_data.get('password', '')  # Get password field value or empty string if not found
        val_con_pas = cleaned_data.get('confirm_password', '')  # Get confirm_password field value or empty string if not found
        if val_pas != val_con_pas:
            raise forms.ValidationError('Password does not match')
