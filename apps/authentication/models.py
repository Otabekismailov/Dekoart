from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from apps.core.models import TimeStampedModel
from rest_framework_simplejwt.tokens import OutstandingToken


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if phone is None:
            raise TypeError('phone required to phone')

        user = self.model(phone=phone)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        if phone is None:
            raise TypeError('phone is required to phone')
        if password is None:
            raise TypeError('Password is required to phone')
        user = self.create_user(phone=phone, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(
        max_length=30, null=True, blank=True, unique=True)
    outstanding = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = False
        ordering = ["-id"]

    def delete(self, *args, **kwargs):
        OutstandingToken.objects.filter(user=self).delete()
        super(User, self).delete(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.first_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
