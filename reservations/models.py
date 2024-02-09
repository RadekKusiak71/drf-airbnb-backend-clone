from django.db import models
from listings.models import Listing
from users.models import Profile
from phonenumber_field.modelfields import PhoneNumberField


class Reservation(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()
    total_days = models.PositiveIntegerField()
    total_price = models.FloatField()
    guests_coming = models.PositiveIntegerField()
    phone_number = PhoneNumberField()
    payment_status = models.BooleanField(default=False)
