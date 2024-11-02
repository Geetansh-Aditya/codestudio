from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    student_id = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  # Hash the password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return f"Student: {self.username}"

class Teacher(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    teacher_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return f"Teacher: {self.username}"
