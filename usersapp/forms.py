from django import forms
from django.contrib.auth.forms import AuthenticationForm

from usersapp.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']