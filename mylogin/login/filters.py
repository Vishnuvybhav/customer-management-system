import django_filters
from django_filters import DateFilter
from .models import *
class orderfilter(django_filters.FilterSet):
    class Meta:
        model = order
        fields = '__all__'
        exclude= ['customer','Date_created']