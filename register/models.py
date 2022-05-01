from django.db import models
from student.models import Student
from book.models import Book

class Register(models.Model):
    STATUS = [
        ('ISD', 'ISSUED'),
        ('RTD', 'RETURNED'),
    ]

    student_roll_no = models.CharField(max_length=9, null=True)
    book_name = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='ISD')
    action_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Register_{self.id}'
