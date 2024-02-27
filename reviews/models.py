from django.db import models
from reservations.models import Reservation
from users.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    RATE_CHOICES = {
        1: "Bad",
        2: "Poor",
        3: "Nice",
        4: "Good",
        5: "Perfect",
    }
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    description = models.CharField(max_length=360)
    rate = models.PositiveIntegerField(
        default=3,
        choices=RATE_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
