from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'})),
    email = forms.EmailField(max_length=100, help_text='eg. youremail@mail.com',
                             widget=forms.EmailInput(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
