import base64
from smtplib import SMTPException

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.http import BadHeaderError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from rest_framework import generics, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User

from .serializers import (
    PasswordResetRequestSerializer,
    RegisterUserSerializer,
    UserSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    """
    Model View Set for User Model
    """

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ("get", "post", "patch", "delete")
    filter_backends = (SearchFilter,)
    search_fields = ("username", "profile__full_name")

    def retrieve(self, request, username, *args, **kwargs):
        if request.user and username == "me":
            instance = request.user
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAllUser(generics.ListAPIView):
    """
    Get All User
    """

    pagination_class = None
    http_method_names = ("get",)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsAdminUser]


class RegisterUser(generics.CreateAPIView):

    serializer_class = RegisterUserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
