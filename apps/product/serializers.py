from rest_framework import serializers
from .models import ProductRecord


class ProductRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRecord
        fields = '__all__'
