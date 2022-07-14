from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from .models import Durations
from .filters import DurationsFilter


class DurationsList(ListView):
    model = Durations
    template_name = 'durations_list.html'
    context_object_name = 'durations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DurationsFilter(self.request.GET, queryset=self.get_queryset())
        return context
