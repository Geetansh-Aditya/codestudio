from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'student_id', 'course']

    def create(self, validated_data):
        student = Student(**validated_data)

        student.password = validated_data['password']
        student.save()
        return student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'email', 'password', 'teacher_id', 'subject']

    def create(self, validated_data):
        teacher = Teacher(**validated_data)
        teacher.password = validated_data['password']  # Hash the password
        teacher.save()
        return teacher
