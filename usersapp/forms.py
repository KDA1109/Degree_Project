from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from usersapp.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']


class UserSignupForm(UserCreationForm):


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    
  