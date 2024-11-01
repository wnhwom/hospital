from rest_framework import serializers

from backend.models import Patient


class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    contact_info = serializers.CharField()


class PatientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['contact_info']