from django.urls import path
from .views import register_student, register_teacher, login

urlpatterns = [
    path('register/student/', register_student, name='register_student'),
    path('register/teacher/', register_teacher, name='register_teacher'),
    path('login/', login, name='login'),
]
