import secrets
from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    sku = models.CharField(max_length=128, primary_key =True, editable = False, default = secrets.token_urlsafe(16 ))
    title = models.CharField(max_length = 128)
    message = models.TextField()
    full_name = models.CharField(max_length = 128)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'contacts'
        ordering = ['-created_at']

        def __str__(self):
            return self.title