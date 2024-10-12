# student/filters.py

import django_filters
from .models import Student, OTM

class StudentFilter(django_filters.FilterSet):
    talabalik_turi = django_filters.ChoiceFilter(
        field_name='talabalik_turi',
        choices=Student.TALABALIK_TURI_CHOICES,
        label='Talabalik Turi'
    )
    otm = django_filters.ModelChoiceFilter(
        queryset=OTM.objects.all(),
        field_name='otm',
        label='OTM'
    )

    class Meta:
        model = Student
        fields = ['talabalik_turi', 'otm']
