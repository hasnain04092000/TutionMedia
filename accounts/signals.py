from accounts.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile


@receiver(post_save, sender=Account)
def post_profile_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)