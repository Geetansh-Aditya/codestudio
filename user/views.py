from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


@api_view(['POST'])
def register_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # First, try to find the user as a Student
    try:
        user = Student.objects.get(username=username)

        if user.password == password:
            return JsonResponse({'message': 'Login successful!', 'user_type': 'student'})
        else:
            return JsonResponse({'error': 'Invalid password'}, status=400)
    except ObjectDoesNotExist:
        pass  # Continue to check for Teacher if not found as Student

    # Next, try to find the user as a Teacher
    try:
        user = Teacher.objects.get(username=username)
        if user.password == password:
            return JsonResponse({'message': 'Login successful!', 'user_type': 'teacher'})
        else:
            return JsonResponse({'error': 'Invalid password'}, status=400)
    except ObjectDoesNotExist:
        pass  # If not found, proceed to return a 404

    # If user is not found as either Student or Teacher
    return JsonResponse({'error': 'User does not exist'}, status=404)
