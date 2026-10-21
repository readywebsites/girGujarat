from django.db import models

class BookingReservation(models.Model):
    VEHICLE_CHOICES = [
        ('bus', 'Group AC Luxury Bus (Included)'),
        ('private', 'Private AC Cab (Innova/Sedan Upgrade)'),
    ]

    HOTEL_CHOICES = [
        ('standard', 'Deluxe 3★ AC Hotel (Included)'),
        ('heritage', 'Luxury Heritage 4★ Resort'),
    ]

    full_name = models.CharField(max_length=150, help_text="Primary traveler's full name")
    phone = models.CharField(max_length=25, help_text="Contact mobile number")
    email = models.EmailField(help_text="Email address for booking confirmation")
    travel_date = models.DateField(help_text="Scheduled tour departure date")
    travelers_count = models.PositiveIntegerField(default=2, help_text="Number of seats reserved")
    vehicle_choice = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default='bus')
    hotel_category = models.CharField(max_length=20, choices=HOTEL_CHOICES, default='standard')
    total_price = models.PositiveIntegerField(default=19998, help_text="Calculated tour total fare (INR)")
    special_requests = models.TextField(blank=True, default='', help_text="Pickup notes, dietary preferences, senior assistance")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking Reservation'
        verbose_name_plural = 'Booking Reservations'

    def __str__(self):
        return f"Booking #{self.id} — {self.full_name} ({self.travel_date}, {self.travelers_count} guests)"


class TourInquiry(models.Model):
    full_name = models.CharField(max_length=150, help_text="Name of prospective traveler")
    phone = models.CharField(max_length=25, help_text="Callback phone number")
    email = models.EmailField(help_text="Contact email address")
    destination = models.CharField(max_length=200, help_text="Tour package or destination of interest")
    message = models.TextField(blank=True, default='', help_text="Custom itinerary questions or group notes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tour Inquiry'
        verbose_name_plural = 'Tour Inquiries'

    def __str__(self):
        return f"Inquiry #{self.id} — {self.full_name} ({self.destination})"
