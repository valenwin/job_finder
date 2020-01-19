from django.db import IntegrityError
from django.shortcuts import render
from .utils import work, rabota, dou
from .models import City, Speciality, Vacancy, Url, Site


def search_job(request):
    return render(request, 'search.html')


def get_vacancies(request):
    city = City.objects.get(name='Киев')
    speciality = Speciality.objects.get(name='Python')
    url_qs = Url.objects.filter(city=city, speciality=speciality)
    site = Site.objects.all()
    url_work = url_qs.get(site=site.get(name='Work.ua')).url_address
    url_rabota = url_qs.get(site=site.get(name='Rabota.ua')).url_address
    url_dou = url_qs.get(site=site.get(name='Dou.ua')).url_address

    jobs = []
    jobs.extend(work(url_work))
    jobs.extend(rabota(url_rabota))
    jobs.extend(dou(url_dou))

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

