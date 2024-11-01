from rest_framework import viewsets
from backend.permissions import RoleBasedPermissionsMixin
from backend.permissions import HasPermissionByAuthenticatedUserRole


class HospitalGenericViewSet(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet
):
    permission_classes = [HasPermissionByAuthenticatedUserRole]