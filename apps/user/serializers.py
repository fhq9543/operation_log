from rest_framework import serializers
from .models import UserRecord


class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecord
        fields = '__all__'
