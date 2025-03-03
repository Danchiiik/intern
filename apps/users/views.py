from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.serializers import RegistrationSerializer, UserListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationApiView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("You successfully registered", status=status.HTTP_201_CREATED)
        

class AccountsApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)  # Use the new serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
