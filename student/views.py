from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .filters import StudentFilter
from .serializers import (
    StudentCreateSerializer,
    StudentListSerializer,
    StudentDetailSerializer,
    StudentUpdateSerializer,
    StudentAssignSponsorSerializer
)


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentAssignSponsorAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAssignSponsorSerializer
    permission_classes = [permissions.IsAuthenticated]
