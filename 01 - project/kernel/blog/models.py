

# Create your models here.


# Anydesk
# teamspeak
# postgresql + pgadmin
# visualstudio code update


### Method 1
# 1) Back-End Database
# 2) Front-End Template
# Model, Form, Admin, View, Template, test


### Method 2 --> HTML, CSS, Javascript
# 1) Template
# 2) Back-End
# Template, View, JinjaFilter, Model, Form, test

# Template
# Model
import uuid
import secrets

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
from django.urls import reverse

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

class Post(TimeStampedMixin):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # sku = models.CharField(primary_key = True, default = secrets.toekn_urlsafe(15), max_lenth = 32, editable = False)

    # title = models.CharField(db_index=True, max_length = 128, unique_for_month='published_at')
    title = models.CharField(max_length = 128, unique_for_month='published_at', help_text = 'must be unique in a month')
    slug = models.CharField(max_length = 128, unique_for_month='published_at')
    banner = models.ImageField(upload_to = 'blog', null = True, blank = True)
    content = RichTextUploadingField()
    summary = models.CharField(max_length = 128)
    # is_published = models.BooleanField(default = False)# False = Draft & True = Publish
    # status = models.CharField(max_length = 1, choices = POST_STATUS, default = DRAFT)
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)

    # relممنون 
    tag = models.ManyToManyField('Tag', related_name = 'post')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'posts')
    
    # datetime
    published_at = models.DateTimeField(default=timezone.now)


    objects = models.Manager()
    posts = PostPublishedManager()

    class Meta:
        # db_table = 'article'
        ordering = ['-published_at', 'title']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        get_latest_by = ['-published_at']
        #### DB Admin (UML) ###
        # unique_together = (('title', 'category'),)
        # index_together = ["title", 'published_at']
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[ self.slug])


    def __str__(self):
        return self.title

class Comment(TimeStampedMixin):
    # commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    email = models.EmailField()
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    title = models.CharField(max_length= 128, unique = True)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def children(self):
        return Comment.objects.filter(parent = self)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        get_latest_by = ['-created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.title, self.post) 


# ####################################################
# ticketing
# ################################################
class Message(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    answer = models.ForeignKey("self", null = True, blank = True, on_delete = models.SET_NULL)
    ticket = models.ForeignKey("Ticketing", on_delete = models.CASCADE, related_name = 'message')

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
    
    def __str__(self):
        return self.title

class Department (models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True )  

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'
    
    def __str__(self):
        return self.title

    
class Ticketing(models.Model):
    start_date = models.DateField()
    expire_date = models.DateField()
    severity = models.PositiveIntegerField(unique = True)
    # Level (basic, normal, pro, advance, master)
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    department = models.ForeignKey("Department" , on_delete = models.CASCADE, related_name='ticket')
    

    class Meta: 
        ordering = ['-start_date', 'expire_date', 'severity', 'status']
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'
        
    
    def __str__(self): 
        return self.severity
    
class Attachment(models.Model):
    title = models.CharField(max_length = 128)
    attachment = models.FileField(upload_to = 'tickets', 
                                    validators=[FileExtensionValidator(['docx', 'doc', 'pdf', 'jpg', 'png'])], 
                                    help_text = 'supported files: doc, pdf, jpg, png and docx')

    ticket = models.ForeignKey("Ticketing", on_delete = models.CASCADE, related_name = 'attachment')

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'
    
    def __str__(self):
        return self.title
# Model (Done)

# Admin (Done)
### Admin: Actions
### Admin: MixinAction
### Admin: inline --> Comment
### Admin: Extension (Import Export)

# Queryset (Done)
### filter
### all
### lazyload
### order_by
### get
### All query sets explained

# Manager (Done)

#***********
## Research
#***********
# 1. eshterak (1month, 3month, 1year) dynamic)
# 2. post haye rayegan moshahede konad
# 3. 
# ** Ticketing


#------------------------------------------------------

# View (2)
## CRUD (Create Read Update Delete) 5 - 10
## Generic View
## Functional View
## URL

# Template (1)
## Jinja2
### Variable
### For loop
### Condition

# Test (1)
## UnitTest
## Test Coverage

# REST API (1)
## JSON
## HTTP
## Concept
## CRUD


# Design
## HTML
## CSS
## JAVASCRIPT


# Template






