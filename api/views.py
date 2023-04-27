from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Contest


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ContestList(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = serializers.ContestSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contest.objects.all()
    serializer_class = serializers.ContestSerializer