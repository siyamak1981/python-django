from django.db import models


class TimeStampedMixin(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class OrganizedMixin(TimeStampedMixin):
    title = models.CharField(max_length= 128, unique = True)
    slug = models.CharField(max_length = 128, unique = True)


    class Meta:
        abstract = True

