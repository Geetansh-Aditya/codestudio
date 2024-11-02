from django.urls import path
from . import views

urlpatterns = [
    path('execute-contents/', views.execute_contents_file, name='api_execute_contents_file'),
]
