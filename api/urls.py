from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterAPIView,
    SponsorCreateAPIView,
    SponsorListAPIView,
    SponsorDetailAPIView,
    SponsorUpdateAPIView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('sponsors/create/', SponsorCreateAPIView.as_view(), name='sponsor-create'),
    path('sponsors/', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('sponsors/<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),
    path('sponsors/<int:pk>/edit/', SponsorUpdateAPIView.as_view(), name='sponsor-edit'),

]
