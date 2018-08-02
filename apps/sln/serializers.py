from rest_framework import serializers
from utils.serializer import TimestampField
from .models import SlnRecord


class SlnRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlnRecord
        fields = '__all__'
