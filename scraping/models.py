from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name}'


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return f'{self.name}'


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Url(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    url_address = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f'Speciality: {self.speciality} in {self.city} on site {self.site}'


class Vacancy(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, max_length=100, blank=True)
    timestamp = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.title}'
