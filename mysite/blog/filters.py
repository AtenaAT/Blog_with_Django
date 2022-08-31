import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="published", label='تاریخ بیشتر  از', lookup_expr='gte')
    end_date = DateFilter(field_name="published", label='تاریخ کمتر  از', lookup_expr='lte')
    post_name = CharFilter(field_name='title', label='نام پست', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['status', ]
