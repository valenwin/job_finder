from django.shortcuts import render


def home_page(request):
    return render(request, 'base.html')


def search_job(request):
    return render(request, 'search.html')
