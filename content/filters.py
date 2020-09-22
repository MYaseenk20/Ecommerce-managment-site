import django_filters
from django_filters import DateFilter
from .models import *
class OrderFiter(django_filters.FilterSet):
    startdate=DateFilter(field_name='date',lookup_expr='gte')
    enddata=DateFilter(field_name='date',lookup_expr='lte')
    class Meta:
        model= Order
        fields='__all__'
        exclude=['customer','date']

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields='__all__'
        exclude=['email','profilepic']


