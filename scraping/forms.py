from django import forms

from scraping.models import Speciality, City


class FindVacancyForm(forms.Form):
    city = forms.ModelChoiceField(label='City',
                                  queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.ModelChoiceField(label='Specialty',
                                       queryset=Speciality.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
