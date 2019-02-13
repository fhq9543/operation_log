from rest_framework import serializers
from .models import ProofingRecord


class ProofingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofingRecord
        fields = '__all__'
