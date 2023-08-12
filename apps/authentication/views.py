from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from .models import User
from .serializers import RegistrationSerializer, LoginSerializers
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from django.conf import settings
from .utils import get_tokens_for_user, AccessToken
from rest_framework.permissions import IsAuthenticated


class RegisterUser(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        user_data = User.objects.filter(phone=phone)
        if user_data:
            return Response({
                "message": "You are already registered",
            }, status=status.HTTP_409_CONFLICT)
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user.is_active:
            data = get_tokens_for_user(user)
            access_token_lifetime = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']

            response = Response({
                "Success": "Register successful",
            })

            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                max_age=access_token_lifetime.total_seconds(),
                expires=None,
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

            csrf.get_token(request)
            return response


class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializers)
    def post(self, request):
        data = request.data
        response = Response()
        serializers = LoginSerializers(data=data)
        serializers.is_valid()
        phone = data.get('phone', None)
        password = data.get('password', None)
        user = authenticate(phone=phone, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data["access"],
                    max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully"}
                return response
            else:
                return Response({"detail": "This Login is not Register!!"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Invalid Phone or password!!"},
                            status=status.HTTP_404_NOT_FOUND)


# class Logout(APIView):
#     # permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         data=request.COOKIES.get('access_token')
#         response = Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
#         response.delete_cookie(key=data)
#         logout(request)
#         return response


class Logout(APIView):
    def get(self, request):
        access_token = request.COOKIES.get('access_token')
        response = JsonResponse({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        logout(request)
        return response
