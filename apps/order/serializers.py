from rest_framework import serializers
from .models import OrderRecord


class OrderRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRecord
        fields = '__all__'
