import os
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BookingReservation, TourInquiry
from .serializers import BookingReservationSerializer, TourInquirySerializer

class BookingCreateView(generics.CreateAPIView):
    """
    POST /api/bookings/
    Validates and persists tour booking reservation requests to the SQLite database.
    """
    queryset = BookingReservation.objects.all()
    serializer_class = BookingReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "id": instance.id,
                "status": "confirmed",
                "message": "Booking reservation successfully saved to the database.",
                "database_record_id": instance.id,
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class InquiryCreateView(generics.CreateAPIView):
    """
    POST /api/inquiries/
    Validates and persists tour inquiries to the SQLite database.
    """
    queryset = TourInquiry.objects.all()
    serializer_class = TourInquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "id": instance.id,
                "status": "received",
                "message": "Tour inquiry successfully saved to the database.",
                "database_record_id": instance.id,
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


@method_decorator(ensure_csrf_cookie, name='dispatch')
class FrontendIndexView(View):
    """
    Serves the landing page (index.html) and ensures Django's real CSRF cookie
    is attached to the browser for secure form submissions.
    """
    def get(self, request, *args, **kwargs):
        index_file_path = os.path.join(settings.BASE_DIR.parent, 'index.html')
        if os.path.exists(index_file_path):
            with open(index_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return HttpResponse(content, content_type='text/html; charset=utf-8')
        return HttpResponse("Frontend index.html not found.", status=404)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCsrfTokenView(View):
    """
    GET /api/csrf/
    Ensures the csrftoken cookie is issued for decoupled/cross-origin clients.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse('{"status": "ok", "message": "CSRF cookie set"}', content_type='application/json')
