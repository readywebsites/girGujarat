from django.urls import path
from .views import BookingCreateView, InquiryCreateView, GetCsrfTokenView

urlpatterns = [
    path('bookings/', BookingCreateView.as_view(), name='api-bookings'),
    path('inquiries/', InquiryCreateView.as_view(), name='api-inquiries'),
    path('csrf/', GetCsrfTokenView.as_view(), name='api-csrf'),
]

