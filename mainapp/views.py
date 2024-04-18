from django.shortcuts import render

def index(request):
    context = {
        'title': 'SportHub - Главная',
        'content': 'Главная стрница магазина - SportHub'
    }

    return render(request, 'mainapp/index.html', context)

def about(request):
    context = {
        'title': 'SportHub - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст об магазине'
    
    }
    return render(request, 'mainapp/about.html', context)