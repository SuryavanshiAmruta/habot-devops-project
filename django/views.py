from django.db import models
import os


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    guardian_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    learning_difficulty = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name
