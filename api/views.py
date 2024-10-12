from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from .filters import SponsorFilter
from .models import Sponsor
from .serializers import SponsorSerializer, SponsorDetailSerializer, SponsorEditSerializer, UserSerializer


# Homiy sifatida ariza topshirish
class SponsorCreateAPIView(generics.CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [AllowAny]

# user register
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# Homiylar ro`yxati va filtrlash
class SponsorListAPIView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SponsorFilter  

# Homiy haqida ma`lumot 
class SponsorDetailAPIView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    permission_classes = [IsAuthenticated]

# Homiyni tahrirlash 
class SponsorUpdateAPIView(generics.UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorEditSerializer
    permission_classes = [IsAuthenticated]
