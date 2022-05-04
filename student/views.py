from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

#students are not getting deleted-look into this

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        print('student list post request')
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print('student list get request')
        return super().get(request, *args, **kwargs)


class StudentRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        print('student get request')
        obj = self.get_object()
        print(obj.book_set.all())
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print('student delete request')
        return super().delete(request, *args, **kwargs)


