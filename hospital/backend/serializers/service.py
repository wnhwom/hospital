from rest_framework import serializers
from backend.models import Doctor, Service, Visit


class ServiceListSerializer(serializers.Serializer):
    name = serializers.CharField()
    type_of_service = serializers.CharField()


class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price']