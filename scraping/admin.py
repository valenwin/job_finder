from django.contrib import admin
from .models import City, Speciality, Vacancy, Site, Url


class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'specialty', 'timestamp')


admin.site.register(City)
admin.site.register(Speciality)
admin.site.register(Vacancy)
admin.site.register(Site)
admin.site.register(Url)
