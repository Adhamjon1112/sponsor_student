# student/urls.py

from django.urls import path
from .views import (
    StudentCreateAPIView,
    StudentListAPIView,
    StudentDetailAPIView,
    StudentUpdateAPIView,
    StudentAssignSponsorAPIView
)

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('students/<int:pk>/edit/', StudentUpdateAPIView.as_view(), name='student-edit'),
    path('students/<int:pk>/assign-sponsor/', StudentAssignSponsorAPIView.as_view(), name='student-assign-sponsor'),
]
