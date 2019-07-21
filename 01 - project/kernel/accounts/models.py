from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
    

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()
    role = models.ManyToManyField('Role', related_name='user')


class Role(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pic = models.ImageField(upload_to = 'user/profile', null = True, blank = True)
    location = models.CharField(max_length = 128, blank = True , null = True)
    

    def __str__(self):
        return '{}'.format(self.user.email)
    
