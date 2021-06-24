from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    username = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'placeholder':'Ваше имя'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput(attrs={'placeholder':'Повторите пароль'}))
    email = forms.CharField(label="Почта", widget=forms.TextInput(attrs={'placeholder':'Почта'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AuthUser(AuthenticationForm):
    username = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'placeholder':'Ваше имя'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']