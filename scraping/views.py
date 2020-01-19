from django.db import IntegrityError
from django.shortcuts import render
from .utils import work, rabota, dou
from .models import City, Speciality, Vacancy


def search_job(request):
    return render(request, 'search.html')


def get_vacancies(request):
    jobs = []
    jobs.extend(work())
    jobs.extend(rabota())
    jobs.extend(dou())
    city = City.objects.get(name='Киев')
    speciality = Speciality.objects.get(name='Python')
    vacancies = Vacancy.objects.filter(city=city.id, speciality=speciality.id).values('url')
    url_list = [vacancy['url'] for vacancy in vacancies]

    for job in jobs:
        if job['href'] not in url_list:
            vacancy = Vacancy(city=city,
                              speciality=speciality,
                              url=job['href'],
                              title=job['title'],
                              description=job['description'],
                              company=job['company'])
            try:
                vacancy.save()
            except IntegrityError:
                pass

    return render(request, 'vacancies.html', {
        'jobs': jobs
    })

