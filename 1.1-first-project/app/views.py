from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse("time"),
        'Показать содержимое рабочей директории': reverse("workdir")
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'

    return HttpResponse(msg)


def workdir_view(request):
    file_name = []
    path = '.'
    rez = sorted(os.listdir(path))
    for n, item in enumerate(rez):
        file_name.append(f"{n + 1}. {item}\n")

    return HttpResponse(file_name)
