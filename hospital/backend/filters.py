import django_filters as filters

from backend.models import Doctor


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter()

    class Meta:
        model = Doctor
        fields = {
            'last_name' : ['exact', 'icontains'],
            'first_name' : ['exact'],
            'specialization' : ['exact']
        }