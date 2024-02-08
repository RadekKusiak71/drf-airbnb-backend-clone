from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")
