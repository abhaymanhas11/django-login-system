from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupform(UserCreationForm):
    email=forms.EmailField(required=True,label=('Email'))
    password2 = forms.CharField(widget=forms.PasswordInput(),label=('Re-enter Password'))
    class Meta:
        model=User
        fields=['username','first_name','email',]



