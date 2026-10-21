"""
TRAVEL FIRST HOLIDAYS — PRODUCTION DJANGO REST FRAMEWORK (DRF) BACKEND CODE
Copy this code into your Django backend project.

Requirements in Django project:
  pip install djangorestframework django-cors-headers
"""

# ==============================================================================
# 1. models.py
# ==============================================================================
"""
from django.db import models

class BookingReservation(models.Model):
    VEHICLE_CHOICES = [
        ('bus', 'Group AC Luxury Bus'),
        ('private', 'Private AC Cab (Innova/Sedan)'),
    ]
    HOTEL_CHOICES = [
        ('standard', 'Deluxe 3-Star AC'),
        ('heritage', 'Luxury Heritage 4-Star Resort'),
    ]

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    travel_date = models.DateField()
    travelers_count = models.PositiveIntegerField(default=2)
    vehicle_choice = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default='bus')
    hotel_category = models.CharField(max_length=20, choices=HOTEL_CHOICES, default='standard')
    total_price = models.PositiveIntegerField(default=19998)
    special_requests = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.full_name} ({self.travel_date})"


class TourInquiry(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    destination = models.CharField(max_length=200)
    message = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry #{self.id} - {self.full_name} ({self.destination})"
"""

# ==============================================================================
# 2. serializers.py
# ==============================================================================
"""
from rest_framework import serializers
from .models import BookingReservation, TourInquiry

class BookingReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingReservation
        fields = [
            'id', 'full_name', 'phone', 'email', 'travel_date',
            'travelers_count', 'vehicle_choice', 'hotel_category',
            'total_price', 'special_requests', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_phone(self, value):
        cleaned = value.replace(' ', '').replace('-', '')
        if len(cleaned) < 10:
            raise serializers.ValidationError("Enter a valid phone number with at least 10 digits.")
        return value


class TourInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourInquiry
        fields = ['id', 'full_name', 'phone', 'email', 'destination', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
"""

# ==============================================================================
# 3. views.py
# ==============================================================================
"""
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BookingReservation, TourInquiry
from .serializers import BookingReservationSerializer, TourInquirySerializer

class BookingCreateView(generics.CreateAPIView):
    queryset = BookingReservation.objects.all()
    serializer_class = BookingReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "id": serializer.data['id'],
                "status": "confirmed",
                "message": "Booking reservation received successfully.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class InquiryCreateView(generics.CreateAPIView):
    queryset = TourInquiry.objects.all()
    serializer_class = TourInquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "id": serializer.data['id'],
                "status": "received",
                "message": "Tour inquiry received successfully.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
"""

# ==============================================================================
# 4. urls.py
# ==============================================================================
"""
from django.urls import path
from .views import BookingCreateView, InquiryCreateView

urlpatterns = [
    path('api/bookings/', BookingCreateView.as_view(), name='api-bookings'),
    path('api/inquiries/', InquiryCreateView.as_view(), name='api-inquiries'),
]
"""

# ==============================================================================
# 5. settings.py (CORS configuration if frontend is on another port/domain)
# ==============================================================================
"""
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'tours', # your app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # must be near top
    'django.middleware.security.SecurityMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For local testing, or specify CORS_ALLOWED_ORIGINS
"""

