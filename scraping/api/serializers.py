from scraping.models import City, Speciality, Vacancy
from rest_framework import serializers


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'slug')


class SpecialtySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speciality
        fields = ('name', 'slug')


class VacancySerializer(serializers.ModelSerializer):
    city = CitySerializer()
    specialty = SpecialtySerializer()

    class Meta:
        model = Vacancy
        fields = ('city', 'specialty', 'timestamp', 'title', 'url',
                  'description', 'company')
