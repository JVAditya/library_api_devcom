from django.db import models

from student.models import Student

class Book(models.Model):

    SUBJECTS = [
        ('MA', 'MATHEMATICS'),
        ('PH', 'PHYSICS'),
        ('CH', 'CHEMISTRY'),
        ('BB', 'BIOLOGY'),
        ('CS', 'COMPUTER SCIENCE'),
        ('EE', 'ELECTRICAL'),
        ('ME', 'MECHANICAL'),
    ]

    name = models.CharField(max_length=25, unique=True, primary_key=True)
    last_issued = models.DateTimeField(auto_now=False, null=True)
    last_returned = models.DateTimeField(auto_now=False, null=True)
    pages = models.IntegerField()
    copies = models.IntegerField(default=1)
    issued_copies = models.IntegerField(default=0)
    author = models.CharField(max_length=25, default='abc')
    subject = models.CharField(max_length=20, choices=SUBJECTS, default='CS')
    student = models.ManyToManyField(Student)


    def __str__(self):
        return self.name
