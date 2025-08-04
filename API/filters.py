import django_filters

from .models import NajotTalim


class NajotTalimFilter(django_filters.FilterSet):
    Kurs_narxi__gt = django_filters.NumberFilter(field_name='Kurs_narxi', lookup_expr='gt')
    Kurs_narxi__lt = django_filters.NumberFilter(field_name='Kurs_narxi', lookup_expr='lt')


    class Meta:
        model = NajotTalim
        fields = ['Kurs_nomi', 'Kurs_narxi']