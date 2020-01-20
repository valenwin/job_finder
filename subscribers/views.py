from django.shortcuts import redirect, render

from .forms import SubscriberModelForm


def subscribe(request):
    contact_form = SubscriberModelForm()
    if request.method == 'POST':
        contact_form = SubscriberModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('subscribers:subscribe_url')

    return render(request, 'subscribe.html', {
        'form': contact_form
    })
