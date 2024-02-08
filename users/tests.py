from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="123")

    def test_profile_create(self):
        profile1 = Profile.objects.create(user=self.user)
        self.assertEqual(profile1.user, self.user)

    def test_profile_born_date(self):
        profile1 = Profile.objects.create(user=self.user)
        date = "2020-05-17"
        profile1.born_date = date
        profile1.save()
        self.assertEqual(date, str(profile1.born_date))

    def test_profile_bio(self):
        profile1 = Profile.objects.create(user=self.user)
        bio = "This is a test bio."
        profile1.bio = bio
        profile1.save()
        self.assertEqual(bio, profile1.bio)

    def test_profile_work(self):
        profile1 = Profile.objects.create(user=self.user)
        work = "Test Company"
        profile1.work = work
        profile1.save()
        self.assertEqual(work, profile1.work)

    def test_profile_languages(self):
        profile1 = Profile.objects.create(user=self.user)
        languages = "English, Polish"
        profile1.languages = languages
        profile1.save()
        self.assertEqual(languages, profile1.languages)
