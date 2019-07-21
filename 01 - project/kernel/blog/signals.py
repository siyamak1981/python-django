from django.dispatch import receiver
from django.db.models.signals import pre_save
from blog.models import Category


@receiver(post_save, sender = Category)
def my_signal_func(sender, **kwargs):
    print ("hello")