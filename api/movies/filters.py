from django_filters import rest_framework as filter
from .models import Movie


class MovieFilter(filter.FilterSet):
    title = filter.CharFilter(lookup_expr='icontains')
    genre = filter.CharFilter(lookup_expr='icontains')
    year = filter.NumberFilter(lookup_expr='exact')
    year__gt = filter.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = filter.NumberFilter(field_name='year', lookup_expr='lt')
    owner__username = filter.CharFilter(lookup_expr='icontains')
    start__gt = filter.NumberFilter(field_name='start', lookup_expr='gt')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'year__gt', 'year__lt', 'owner__username', 'start__gt']
