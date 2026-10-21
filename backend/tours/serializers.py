import re
from rest_framework import serializers
from .models import BookingReservation, TourInquiry

class BookingReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingReservation
        fields = [
            'id',
            'full_name',
            'phone',
            'email',
            'travel_date',
            'travelers_count',
            'vehicle_choice',
            'hotel_category',
            'total_price',
            'special_requests',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_full_name(self, value):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise serializers.ValidationError("Full name must contain at least 2 characters.")
        return cleaned

    def validate_phone(self, value):
        cleaned = re.sub(r'[\s\-\(\)]', '', value)
        if len(cleaned) < 10:
            raise serializers.ValidationError("Please provide a valid phone number with at least 10 digits.")
        return value

    def validate_travelers_count(self, value):
        if value < 1:
            raise serializers.ValidationError("Reservation must have at least 1 traveler.")
        if value > 50:
            raise serializers.ValidationError("For groups over 50, please contact our charter team directly.")
        return value


class TourInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourInquiry
        fields = [
            'id',
            'full_name',
            'phone',
            'email',
            'destination',
            'message',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_full_name(self, value):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise serializers.ValidationError("Full name must contain at least 2 characters.")
        return cleaned

    def validate_phone(self, value):
        cleaned = re.sub(r'[\s\-\(\)]', '', value)
        if len(cleaned) < 10:
            raise serializers.ValidationError("Please provide a valid phone number with at least 10 digits.")
        return value

