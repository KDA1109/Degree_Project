from django.shortcuts import render

def login(request):
    context = {
        'title': 'Авторизация'
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