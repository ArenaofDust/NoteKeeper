from django.contrib.auth.models import User

#Serializer takes JSON data and converts it into python code and vice versa
from rest_framework import serializers
from .models import Note

#Inherits from serializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    #Method that creates new user by accepting validated data from serializer
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}