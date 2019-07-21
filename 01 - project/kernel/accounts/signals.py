from django.contrib.auth models import User
from accounts.models import User
from django.db.models.signals import recevier, post_save


@receiver(post_save, sender = user)
def create_or_update_profile(sender, instance, create, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()
