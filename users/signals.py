from django.db.models.signals import post_save, pre_delete, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, using, **kwargs):
    if instance.user:
        instance.user.delete()
        print("User deleted")
