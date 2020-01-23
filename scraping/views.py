from datetime import date

from django.http import Http404
from django.shortcuts import render
from .utils import work, rabota, dou
from .models import City, Speciality, Url, Site
from .forms import FindVacancyForm


def search_vacancies(request):
    today = date.today()
    form = FindVacancyForm()

    if request.GET:

        try:
            city_id = int(request.GET.get('city'))
            speciality_id = int(request.GET.get('specialty'))
        except ValueError:
            raise Http404('Unknown query...')

        city = City.objects.get(id=city_id)
        speciality = Speciality.objects.get(id=speciality_id)

        url_qs = Url.objects.filter(city=city, speciality=speciality)
        site = Site.objects.all()
        url_work = url_qs.get(site=site.get(name='Work.ua')).url_address
        url_rabota = url_qs.get(site=site.get(name='Rabota.ua')).url_address
        url_dou = url_qs.get(site=site.get(name='Dou.ua')).url_address

        jobs = []
        jobs.extend(work(url_work))
        jobs.extend(rabota(url_rabota))
        jobs.extend(dou(url_dou))

        jobs_qty = len(jobs)

        return render(request, 'search_vacancies.html', {
            'form': form,
            'jobs': jobs,
            'today': today,
            'jobs_qty': jobs_qty
        })

    return render(request, 'search_vacancies.html', {
        'form': form
    })

