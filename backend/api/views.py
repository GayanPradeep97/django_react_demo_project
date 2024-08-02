from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerilizer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

#User Create
class CreateUserView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


#Note create
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerilizer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)

        else:
            print(serializer.errors)    


#Note Delete
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerilizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    
            