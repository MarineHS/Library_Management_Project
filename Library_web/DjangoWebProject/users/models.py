from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

#Change superuser
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser requires is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser requires is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# User model with authentification by email
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField()
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "date_birth"
        ]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"