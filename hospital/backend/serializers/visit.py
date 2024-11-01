from rest_framework import serializers
from .models import Doctor, Service, Visit


class VisitListSerializer(serializers.Serializer):
    visit_date = serializers.DateTimeField()
    status = serializers.CharField()


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['visit_date']