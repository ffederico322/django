from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Страница приложения women')


def categories(request, cat_id):
    return HttpResponse(f'Статьи по категориям, id {cat_id}')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'Статьи по категориям, slug {cat_slug}')


def archive(request, year):
    return HttpResponse(f'Статьи по категориям, год {year}')



