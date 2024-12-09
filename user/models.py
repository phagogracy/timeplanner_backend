import secrets
import string

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel

from user.manager import CustomAccountManager


def generate_random_username(length=8):
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))

class User(AbstractBaseUser, SafeDeleteModel, PermissionsMixin):
    """
    Custom Account User: email, first_name, last_name, username, is_staff, phone, address, avatar
    """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email if self.email is not None else "No Email"

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        """
        Meta
        """

        ordering = ["created_on"]

    def save(self, keep_deleted=False, **kwargs):
        if not self.username:
            self.username = self.generate_unique_username()
        return super().save(keep_deleted, **kwargs)
    
    def generate_unique_username(self):
        username = generate_random_username()
        while self.__class__.objects.filter(username=username).exists():
            username = generate_random_username()
        return username