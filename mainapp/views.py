from django.shortcuts import render

def index(request):
    context = {
        'title': 'SportHub - Главная',
        'content': 'Спорт - наше всё! SportHub знает об этом лучше всех!'
    }

    return render(request, 'mainapp/index.html', context)

def about(request):
    context = {
        'title': 'SportHub - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст об магазине'
    
    }
    return render(request, 'mainapp/about.html', context)