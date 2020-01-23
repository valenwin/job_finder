from django.urls import path
from .views import search_vacancies

urlpatterns = [
    path('vacancies', search_vacancies, name='search_job_url'),

]
