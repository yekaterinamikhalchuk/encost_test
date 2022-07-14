from django.forms import SelectDateWidget, SplitDateTimeWidget, Select, TimeInput
from django_filters import FilterSet, DateFilter, DateTimeFilter, TimeFilter, RangeFilter,NumberFilter, CharFilter
from .models import Durations, Clients


class DurationsFilter(FilterSet):
    start = DateFilter(field_name='start',
                               label='Start date',
                               widget=SelectDateWidget)
    stop = DateFilter(field_name='stop',
                       label='Stop date',
                       widget=SelectDateWidget)
    stop1 = TimeFilter(field_name='stop', label='start hour', widget=TimeInput, lookup_expr='hour')
    # client = ModelChoiceFilter(queryset=Clients.objects.all())
    # post_text = CharFilter(label='Text', lookup_expr='')
    # minutes = CharFilter(lookup_expr='gt', widget=TimeInput)

    class Meta:
        model = Durations
        fields = (
            'client',
            'equipment',
            'mode',
            'minutes',
            'start',
            'stop',
            'stop1',
            'minutes')