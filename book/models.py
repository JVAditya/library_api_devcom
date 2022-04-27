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
    acquired = models.DateTimeField(auto_now_add=True)
    issued = models.DateTimeField(auto_now=True)
    last_returned = models.DateTimeField(auto_now=True)
    pages = models.IntegerField()
    copies = models.IntegerField(default=1)
    author = models.CharField(max_length=25, default='abc')
    subject = models.CharField(max_length=20, choices=SUBJECTS, default='CS')
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
