from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #List of all objects when creating new user
    serializer_class = UserSerializer #Tells view what data to accept when making new user
    permission_classes = [AllowAny] #Allows anyone to use view to create new user