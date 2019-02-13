from rest_framework import serializers
from .models import AggregatorCaseRecord


class AggregatorCaseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatorCaseRecord
        fields = '__all__'
