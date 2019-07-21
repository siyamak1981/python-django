from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'


def ready(self):
    # from blog.signals import my_signal_func
    # from blog.models import Category

    # post_save.connect(my_signal_func, sender = Category)
    from blog import signals