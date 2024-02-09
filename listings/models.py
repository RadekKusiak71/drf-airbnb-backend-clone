from django.db import models
from cities_light.models import Country, City
from users.models import Profile
from django.core.validators import FileExtensionValidator


def get_listing_upload_path(instance, filename):
    return f'{instance}/{filename}'


class Listing(models.Model):
    CHECK_IN_CHOICES = (
        ("Independent", "Independent"),
        ("Meeting", "Meeting"),
    )
    street = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    price = models.FloatField()
    check_in = models.CharField(max_length=20, choices=CHECK_IN_CHOICES)
    guests_count = models.PositiveIntegerField(default=1)
    beds_count = models.PositiveIntegerField(default=1)
    toilets_count = models.PositiveIntegerField(default=1)
    description = models.TextField()
    parking = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)

    def __str__(self):
        return f'listing #{self.id} - {self.city},{self.country} '


class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="images", default=None)
    image = models.ImageField(upload_to=get_listing_upload_path, validators=[
                              FileExtensionValidator(['png', 'jpeg', 'jpg'])])

    def __str__(self):
        return f'listing #{self.listing.id} image'
