import datetime
import os

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer,RegisterSerializer 
from .models import User

class LoginApi(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if serializer.is_valid():
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')

                # Authenticate user
                user = authenticate(username=username, password=password)

                if user:
                    # Generate JWT tokens
                    jwt_token = RefreshToken.for_user(user)

                    # Token response
                    return Response(
                        {
                            "message": "Login successful",
                            "data": {
                                'created': datetime.datetime.fromtimestamp(jwt_token['iat'], tz=datetime.timezone.utc),
                                'expires': datetime.datetime.fromtimestamp(jwt_token['exp'], tz=datetime.timezone.utc),
                                'refresh': str(jwt_token),
                                'access': str(jwt_token.access_token),
                            }
                        },
                        status=status.HTTP_200_OK
                    )
                return Response({"message": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response(
                {
                    "message": "Invalid data",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegistrationView(APIView):

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)

            if serializer.is_valid():
                user = serializer.save()  # Create the user
                return Response({
                    "message": "Registration successful",
                    "data": {
                        "username": user.username,
                        "email": user.email
                    }
                }, status=status.HTTP_201_CREATED)

            return Response({
                "message": "Registration failed",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
