
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Passwored (again)',widget=forms.PasswordInput(attrs={'class':'form-control mt-2 p-2'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control mt-2 p-2'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control mt-2 p-2'}),
            'last_name':forms.TextInput(attrs={'class':'form-control mt-2 p-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control mt-2 p-2'}),
            'username':forms.TextInput(attrs={'class':'form-control mt-2 p-2'}),
           
        }