from rest_framework import generics, status
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from api.models import User
from .serializer import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import APIView, permission_classes
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate


class HomePageView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")
    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
   

'''class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'message': 'This is a protected endpoint.',
            'user': str(request.user),  # Access user information
        }
        return Response(data)'''


  



