from rest_framework import serializers
from .models import ImportRecord, ExportRecord


class ImportRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportRecord
        fields = '__all__'


class ExportRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportRecord
        fields = '__all__'
