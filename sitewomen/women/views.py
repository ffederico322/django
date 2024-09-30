from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Страница приложения women')


def categories(request):
    return HttpResponse('Страница с категориями')


