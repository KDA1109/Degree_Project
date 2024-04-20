from django.shortcuts import render

from goodsapp.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'SportHub - Главная',
        'content': 'Спорт - наше всё! SportHub знает об этом лучше всех!',
        'categories': categories
    }

    return render(request, 'mainapp/index.html', context)

def about(request):
    context = {
        'title': 'SportHub - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст об магазине'
    
    }
    return render(request, 'mainapp/about.html', context)