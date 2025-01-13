from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm,
    AuthenticationForm,
)



# local imports
from accounts.models import CustomUser



# two forms: register form and login form


class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "form-control"}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
                attrs={'placeholder': "Password", 'class': "form-control", 'data-toggle': "password", 'id':"password"}))

    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
                attrs={'placeholder': "Password", 'class': "form-control", 'data-toggle': "password", 'id':"password2"}
            ))

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password',}
        ))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", )





class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", )