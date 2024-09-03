from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, Loginserializer
from .models import SignupUser  # Ensure this is the model

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

class SignupUserView(APIView):  # Renamed to avoid conflict
    def post(self, request):
        data = request.data
        email = data.get('email')

        # Check if email already exists
        if SignupUser.objects.filter(email = email).exists():
            return Response({"error": "Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with user creation if email is unique
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "User registered successfully")
            return redirect('login') # Redirect to the login page or any other URL
        else:
            return Response({"error": "user registration failed.", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        email = request.query_params.get('email')
        if email:
            try:
                user = SignupUser.objects.get(email=email)  # Reference the correct model
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except SignupUser.DoesNotExist:  # Correctly handling the exception
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Please provide an email."}, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request):
        serializer = Loginserializer(data = request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # create or get token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "success" : "Login success",
                "token": token.key
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,

        }
        return Response(user_data, status=status.HTTP_200_OK)

class UserProfileNew(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(SignupUser, pk=user_id)
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(user_data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"details": "Successfully logout."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"details": "invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        
class ResetPassword(APIView):
    def post(self, request):
        email = request.data.get('email')
        print(email)
