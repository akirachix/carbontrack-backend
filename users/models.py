from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
from factory.models import Factory
from django.core.validators import RegexValidator



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        extra_fields.setdefault("user_type", "manager")
        return self.create_user(email, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ("manager", "KTDA Manager"),
        ("factory", "Factory Manager"),
    )
    factory= models.ForeignKey("factory.Factory", on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
    validators=[phone_regex],
    max_length=15,
    unique=True,
    blank=True,
    null=True
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
    upload_to = 'profiles/',    
    blank=True,
    null=True,
    default="profiles/default.png"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        if self.user_type == "factory" and not self.factory:
            raise ValidationError("Factory is required for factory managers.")
        if self.user_type == "manager" and self.factory:
            raise ValidationError("KTDA Managers should not be linked to a factory")
            

    def __str__(self):
        return f"{self.email} ({self.user_type})"


