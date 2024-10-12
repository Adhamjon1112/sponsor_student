# sponsors/filters.py

import django_filters
from .models import Sponsor

class SponsorFilter(django_filters.FilterSet):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('moderatsiya', 'Moderatsiyada'),
        ('tasdiqlangan', 'Tasdiqlangan'),
        ('bekor_qilingan', 'Bekor qilingan'),
    ]

    PAYMENT_AMOUNT_CHOICES = [
        ('1000000', '1 000 000 UZS'),
        ('5000000', '5 000 000 UZS'),
        ('7000000', '7 000 000 UZS'),
        ('10000000', '10 000 000 UZS'),
        ('30000000', '30 000 000 UZS'),
        ('50000000', '50 000 000 UZS'),
    ]

    status = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES,
        label="ARIZA HOLATI",
        method='filter_status',
        empty_label="Barchasi", 
        required=False         
    )
    payment_amount = django_filters.ChoiceFilter(
        choices=PAYMENT_AMOUNT_CHOICES,
        label="HOMIYLIK SUMMASI",
        method='filter_payment_amount',
        empty_label="Barchasi",  
        required=False,          
    )
    date = django_filters.DateFromToRangeFilter(
        label="SANA",
        field_name='date'
    )

    class Meta:
        model = Sponsor
        fields = ['status', 'payment_amount', 'date']

    def filter_status(self, queryset, name, value):
        if value:
            return queryset.filter(status=value)
        return queryset

    def filter_payment_amount(self, queryset, name, value):
        if value:
            return queryset.filter(payment_amount=value)
        return queryset
