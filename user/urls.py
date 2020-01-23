from django.urls import path
from .views import sign_up, sign_in, sign_out


urlpatterns = [
    path('registration', sign_up, name='sign_up_url'),
    path('login', sign_in, name='sign_in_url'),
    path('logout', sign_out, name='sign_out_url')

]
