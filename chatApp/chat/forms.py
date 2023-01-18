from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #first_name = forms.CharField(max_length=200)
    Nom = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['Nom','username','email','password1','password2']