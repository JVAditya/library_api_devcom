
from django.shortcuts import render
from rest_framework import generics

from student.models import Student

from .models import Book
from .serializers import BookPostSerializer, BookPutSerializer
from register.serializers import RegisterSerializer
from datetime import datetime
from pytz import timezone
from rest_framework.response import Response

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookPostSerializer

    def get(self, request, *args, **kwargs):
        print('book list get request')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for instance in queryset:
            if instance.name == request.data['name']:
                if instance.pages != int(request.data['pages']) or instance.author != request.data['author'] or \
                    instance.subject != request.data['subject']:
                    raise ValueError("Book details can't be mutated")
                instance.copies += int(request.data['copies'])
                instance.save()
                serializer = BookPostSerializer(instance=instance)
                return Response(data=serializer.data)


        print('book list post request')
        return super().post(request, *args, **kwargs)

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookPutSerializer
    

    def get(self, request, *args, **kwargs):
        print('book get request')
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        book_obj = self.get_object()
        if book_obj.student is not None:
            if request.data['student'] != '':
                raise ValueError('Book is already given to a student')
            else:
                serializer = RegisterSerializer(data={
                    'student_roll_no':book_obj.student.roll_no,
                    'book_name':book_obj.name,
                    'status':'RTD',
                })
                serializer.is_valid()
                serializer.save()
                book_obj.last_returned = datetime.now(timezone('Asia/Kolkata'))
                book_obj.save()

        else:
            
            serializer = RegisterSerializer(data={
                'student_roll_no':request.data['student'],
                'book_name':book_obj.name,
                'status':'ISD',
            })
            serializer.is_valid()
            serializer.save()
            book_obj.last_issued = datetime.now(timezone('Asia/Kolkata'))
            book_obj.save()

        

        print('book put request')
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        book_obj = self.get_object()
        if book_obj.student is not None:
            if request.data['student'] != '':
                raise ValueError('Book is already given to a student')
            else:
                serializer = RegisterSerializer(data={
                    'student_roll_no':book_obj.student.roll_no,
                    'book_name':book_obj.name,
                    'status':'RTD',
                })
                serializer.is_valid()
                serializer.save()
                book_obj.last_returned = datetime.now(timezone('Asia/Kolkata'))
                book_obj.save()

        else:
            
            serializer = RegisterSerializer(data={
                'student_roll_no':request.data['student'],
                'book_name':book_obj.name,
                'status':'ISD',
            })
            serializer.is_valid()
            serializer.save()
            book_obj.last_issued = datetime.now(timezone('Asia/Kolkata'))  #not working
            book_obj.save()

        print('book patch request')
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        book_obj = self.get_object()
        if book_obj.student is not None:
            raise ValueError("Cannot remove because a student is using it")
        print('book delete request')
        return super().delete(request, *args, **kwargs)