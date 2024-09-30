from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse


def index(request):
    return HttpResponse('Страница приложения women')


def categories(request, cat_id):
    return HttpResponse(f'Статьи по категориям, id {cat_id}')


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f'Статьи по категориям, slug {cat_slug}')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)
    return HttpResponse(f'Статьи по категориям, год {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')



