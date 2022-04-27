from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        print('book list get request')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('book list post request')
        return super().post(request, *args, **kwargs)

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        print('book get request')
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        
        print('book put request')
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print('book patch request')
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print('book delete request')
        return super().delete(request, *args, **kwargs)