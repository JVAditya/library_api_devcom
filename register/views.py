from django.shortcuts import render
from rest_framework import generics
from .models import Register
from .serializers import RegisterSerializer

class RegisterListAPIView(generics.ListAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer



