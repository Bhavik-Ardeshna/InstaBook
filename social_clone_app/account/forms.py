from . import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }


class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(), max_length=50, required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(), max_length=50, required=False)
    location = forms.CharField(
        widget=forms.TextInput(), max_length=25, required=False)
    url = forms.URLField(widget=forms.TextInput(),
                         max_length=60, required=False)
    profile_info = forms.CharField(
        widget=forms.TextInput(), max_length=260, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'first_name', 'last_name',
                  'location', 'url', 'profile_info')
