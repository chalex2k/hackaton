from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Contest


class ContestSerializer(serializers.ModelSerializer):
    organizer_name = serializers.ReadOnlyField(source='organizer.name')

    class Meta:
        model = Contest
        fields = ['id', 'name', 'description', 'datetime_start', 'datetime_end', 'city', 'format', 'feeding',
                  'difficulty', 'type', 'organizer_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
