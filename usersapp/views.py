from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserLoginForm, UserSignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from cartsapp.models import Cart


def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, f'{username} Вы вошли в аккаунт.')
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('usersapp:logout'):
                    return HttpResponseRedirect(reverse('mainapp:index'))
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
        
    }
    return render(request, 'usersapp/login.html', context)



def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{request.user.username} Поздравляем! Вы успешно зарегистрировались.')
            return HttpResponseRedirect(reverse('usersapp:login'))
    else:
        form = UserSignupForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'usersapp/signup.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен.')
            return HttpResponseRedirect(reverse('usersapp:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Личный Кабинет',
        'form': form
    }
    return render(request, 'usersapp/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f'{request.user.username} Вы вышли из аккаунта.')
    auth.logout(request)
    return redirect(reverse('mainapp:index'))


def user_cart(request):
    return render(request, 'usersapp/users_cart.html')