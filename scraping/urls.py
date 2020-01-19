from django.urls import path
from .views import search_job, vacancy_list

urlpatterns = [
    path('', search_job, name='search_job_url'),
    path('vacancies', vacancy_list, name='vacancy_list_url'),

]
