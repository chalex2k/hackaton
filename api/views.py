from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, permissions
from rest_framework_simplejwt import authentication

from . import serializers
from django.contrib.auth.models import User
from .models import ContestModel
from .serializers import ContestSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(responses={
        status.HTTP_200_OK: serializer_class,
        status.HTTP_401_UNAUTHORIZED: {}})
    def get(self, request):
        return self.list(request)


class UserDetailView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(responses={
        status.HTTP_200_OK: serializer_class,
        status.HTTP_401_UNAUTHORIZED: {}})
    def get(self, request):
        pass


class ContestListView(generics.ListCreateAPIView):
    queryset = ContestModel.objects.all()
    serializer_class = ContestSerializer

    @swagger_auto_schema(responses={
        status.HTTP_200_OK: serializer_class,
        status.HTTP_401_UNAUTHORIZED: {}})
    def get(self, request):
        return self.list(request)


class ContestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContestModel.objects.all()
    serializer_class = serializers.ContestSerializer

    def get(self, request):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class FavoritesView(generics.GenericAPIView):
    pass