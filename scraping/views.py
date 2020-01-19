from django.shortcuts import render
from .utils import djinni, work
from .models import City, Speciality, Vacancy


def search_job(request):
    return render(request, 'search.html')


def get_vacancies(request):
    jobs = work()
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
            vacancy.save()

    return render(request, 'vacancies.html', {
        'jobs': jobs
    })
