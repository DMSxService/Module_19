from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator


class ClassPlatform(TemplateView):
    head = 'Главная страница'
    cont = ''
    template_name = 'platform.html/'
    extra_context = {'head': head, 'cont': cont}


def func_games(request):
    head = 'Игры'
    button1 = "Купить"
    games = []
    games_all = Game.objects.all()
    for i in range(len(games_all)):
        games.append(f'{games_all[i].title} | '
                     f'{games_all[i].description} Стоимость: {games_all[i].cost}')
    context = {
        'head': head,
        'games': games,
        'b1': button1
    }
    return render(request, 'games.html', context)


def news(request):
    news_all = News.objects.all().order_by('-date')
    paginator = Paginator(news_all,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'news': page_obj}
    return render(request, 'news.html', context)


class ClassCart(TemplateView):
    head = 'Корзина'
    cont = 'Извините, ваша корзина пуста'
    template_name = 'cart.html'
    extra_context = {'head': head, 'cont': cont}


info = {}
users = []


def sign_up_by_django(request):
    global info
    error = ""
    buyers = Buyer.objects.all()
    for i in range(len(buyers)):
        users.append(buyers[i].name)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            greeting = f'Приветствуем,{username} !'
            if username in users:
                error = 'Пользователь уже существует'
                greeting = ''
            if password != repeat_password:
                error = 'Пароли не совпадают'
                greeting = ''
            if int(age) < 18:
                error = 'Вы должны быть старше 18'
                greeting = ''
            if error == "":
                Buyer.objects.create(name=username, balance=0, age=age)
            info = {'form': form, 'greeting': greeting, 'error': error,
                    'username': username, 'password': password,
                    'repeat_password': repeat_password, 'age': age}
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    global info
    error = ""
    buyers = Buyer.objects.all()
    for i in range(len(buyers)):
        users.append(buyers[i].name)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        greeting = f'Приветствуем,{username} !'
        if username in users:
            error = 'Пользователь уже существует'
            greeting = ''
        if password != repeat_password:
            error = 'Пароли не совпадают'
            greeting = ''
        if int(age) < 18:
            error = 'Вы должны быть старше 18'
            greeting = ''
        if error == "":
            Buyer.objects.create(name=username, balance=0, age=age)
        info = {'greeting': greeting, 'error': error,
                'username': username, 'password': password,
                'repeat_password': repeat_password, 'age': age}
        return render(request, 'registration_page.html', info)
    return render(request, 'registration_page.html')
