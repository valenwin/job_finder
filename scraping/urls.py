from django.urls import path
from .views import search_job, get_vacancies

urlpatterns = [
    path('', search_job, name='search_job_url'),
    path('vacancies/', get_vacancies, name='get_vacancies_url'),

]
