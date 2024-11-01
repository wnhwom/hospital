from rest_framework import generics
from backend.models import Doctor
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from backend.permissions import RoleBasedPermissionsMixin, HasPermissionByAuthenticatedUserRole
from backend.serializers.doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorUpdateSerializer,DoctorCreateSerializer
from backend.serializers.patient import PatientListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from backend.filters import DoctorFilterSet


class DoctorView(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = [DjangoFilterBackend]
    permission_classes = [HasPermissionByAuthenticatedUserRole]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet




    def get_action_permission(self):
        if self.action in ('list','retrieve'):
            self.action_permissions = ['view_doctor']
        elif self.action == 'list_patient':
            self.action_permissions  = ['view_patient']
        else:
            self.action_permissions = []


    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.prefetch_related('visits').all()

        return Doctor.objects.all()

    def list_patient(self,request,id):
        queryset = self.get_queryset().filter(visits__doctor_id= id)


        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)