from django import forms

from scraping.models import Speciality, City
from .models import Subscriber


class SubscriberModelForm(forms.ModelForm):
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(
                                 attrs={"class": 'form-control'}
                             ))
    city = forms.ModelChoiceField(label='City',
                                  queryset=City.objects.all(),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control'}
                                  ))
    speciality = forms.ModelChoiceField(label='Speciality',
                                        queryset=Speciality.objects.all(),
                                        widget=forms.Select(
                                            attrs={'class': 'form-control'}
                                        ))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}
                               ))
    is_active = forms.BooleanField(label='I agree to receive the newsletter with vacancies on my email',
                                   required=True,
                                   widget=forms.CheckboxInput(
                                       attrs={'class': 'form-check-input', 'checked': 'checked'}
                                   ))

    class Meta:
        model = Subscriber
        fields = ('email', 'city', 'specialty', 'password', 'is_active')
