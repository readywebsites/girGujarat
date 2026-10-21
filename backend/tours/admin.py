from django.contrib import admin
from .models import BookingReservation, TourInquiry

@admin.register(BookingReservation)
class BookingReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'travel_date', 'travelers_count', 'vehicle_choice', 'hotel_category', 'total_price', 'created_at')
    list_filter = ('vehicle_choice', 'hotel_category', 'travel_date', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'special_requests')
    readonly_fields = ('created_at',)
    date_hierarchy = 'travel_date'


@admin.register(TourInquiry)
class TourInquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'destination', 'created_at')
    list_filter = ('destination', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
