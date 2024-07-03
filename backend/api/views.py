from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView): #view lists all notes user has created or creates new notes
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) #Gets all notes written by user
    
    #Gets access to serializer object and checks if valid
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) #saves serializer and makes new version of note, adds author
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) #Gets all notes written by user



            
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #List of all objects when creating new user
    serializer_class = UserSerializer #Tells view what data to accept when making new user
    permission_classes = [AllowAny] #Allows anyone to use view to create new user