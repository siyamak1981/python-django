import uuid
import secrets
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin
from painless.models.managers import PostPublishedManager
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

status = options.PostStatus(is_charfield = False)


class Tag(OrganizedMixin):
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Category(OrganizedMixin):
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title


class Roles(models.Model):
    title = models.CharField(max_length = 32)
    content = models.TextField()
    firstname = models.CharField(max_length = 32)
    lastname = models.CharField(max_length = 32)
    bio = RichTextUploadingField()
    birthday = models.DateTimeField(auto_now_add=True)
    biopic = models.ImageField(upload_to = 'bio', null = True, blank = True)
    
    class Meta: 
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
      
    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length = 32)
    province = models.CharField(max_length = 32)


class Bosses(models.Model):
    role = models.ForeignKey('Roles', on_delete = models.PROTECT, related_name = 'bosses')
    city = models.ForeignKey('City', on_delete = models.PROTECT, related_name = 'boss')
    
    class Meta:
        ordering = ['role', 'city']
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'
        

class Post(TimeStampedMixin):
    # uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 128, unique_for_month='published_at', help_text = 'must be unique in a month')
    slug = models.CharField(max_length = 128, unique_for_month='published_at')
    banner = models.ImageField(upload_to = 'sport', null = True, blank = True)
    content = RichTextUploadingField()
    summary = models.CharField(max_length = 128)
    
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)

    tag = models.ManyToManyField('Tag', related_name = 'post')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'posts')
    author = models.ForeignKey('Bosses', on_delete=models.CASCADE, related_name = 'Bosses')

    published_at = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    posts = PostPublishedManager()

    class Meta:

        ordering = ['-published_at', 'title']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        get_latest_by = ['-published_at']


    def __str__(self):
        return self.title

