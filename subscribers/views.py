from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SubscriberModelForm
from .models import Subscriber


class SubscriberCreate(CreateView):
    model = Subscriber
    form_class = SubscriberModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('create')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            messages.success(request, 'Data was saved successfully.')
            return self.form_valid(form)
        else:
            messages.error(request, 'Check if the form was filled out correctly.')
            return self.form_invalid(form)
