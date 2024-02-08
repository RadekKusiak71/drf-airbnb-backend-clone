from django.db import models
from django.contrib.auth.models import User
from cities_light.models import Country, City


class Profile(models.Model):
    """
        Profile model is extending a User and adding additional fields

        Explanation:

            user -> ForeignKey to User model

            - Not required fields:
            born_date -> Date field to store user birthday
            bio -> Short text (max 400 chars) about user
            work -> User workplace not
            school -> User current school or last school that he attended to
            passion -> User passion
            fun_fuct -> short fun fact about user
            favourite_song -> favourite song
            book_title -> Favourite book title
            pets -> Pets that user have
            language -> language that user speaks in

            # django-cities-light doc https://django-cities-light.readthedocs.io/en/stable-3.x.x/full.html#models
            country -> Place of living
            city -> Place of living

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    born_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    work = models.CharField(max_length=40, null=True, blank=True)
    school = models.CharField(max_length=40, null=True, blank=True)
    passion = models.CharField(max_length=40, null=True, blank=True)
    fun_fact = models.CharField(max_length=40, null=True, blank=True)
    favourite_song = models.CharField(max_length=40, null=True, blank=True)
    book_title = models.CharField(max_length=40, null=True, blank=True)
    pets = models.CharField(max_length=40, null=True, blank=True)
    languages = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} #{self.id}'
