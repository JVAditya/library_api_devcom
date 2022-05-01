from dataclasses import fields
from rest_framework import serializers
from .models import Book

class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        read_only_fields = [
            'last_issued',
            'last_returned',
            'student',
        ]

class BookPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        read_only_fields = [
            'name',
            'last_issued',
            'last_returned',
            'pages',
            'copies',
            'author',
            'subject',
        ]