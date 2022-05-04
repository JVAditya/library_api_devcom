from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25)
    roll_no = models.CharField(max_length=9, unique=True, primary_key=True)

    def __str__(self):
        return self.name
