from backend.mixin import HospitalGenericViewSet
from rest_framework import viewsets, mixins,filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.filters import DoctorFilterSet
from backend.serializers.patient import PatientListSerializer,PatientRetrieveSerializer,PatientCreateSerializer,PatientUpdateSerializer
from backend.models import Patient


class PatientView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_field = ['first_name', 'last_name']



    def get_action_permission(self):
        if self.action in ('list','retrieve'):
            self.action_permissions = ['view_patient']
        elif self.action == 'create':
            self.action_permissions  = ['add_patient']
        elif self.action == 'update':
            self.action_permissions = ['change_patient']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient']
        else:
            self.action_permissions = []


    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'update':
            return PatientUpdateSerializer

    def get_queryset(self):
        return Patient.objects.all()

    def list_patient(self,request,id):
        queryset = self.get_queryset().filter(visits__doctor_id= id)


        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)