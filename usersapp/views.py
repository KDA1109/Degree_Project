from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'usersapp/login.html', context)



def signup(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'usersapp/signup.html', context)


def profile(request):
    context = {
        'title': 'Личный Кабинет'
    }
    return render(request, 'usersapp/profile.html', context)


def logout(request):
    ...