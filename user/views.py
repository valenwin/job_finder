from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            sign_up_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Visitor')
            customer_group.user_set.add(sign_up_user)
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {
        'form': form
    })


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('scraping:search_job_url')
            else:
                redirect('user:sign_up_url')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {
        'form': form
    })


def sign_out(request):
    logout(request)
    return redirect('user:sign_in_url')
