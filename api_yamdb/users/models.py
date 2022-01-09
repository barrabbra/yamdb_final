from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        MODERATOR = 'moderator', _('Moderator')
        USER = 'user', _('User')

    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(
        unique=True,
        blank=True,
        editable=False,
        null=True,
        max_length=36,
    )
    role = models.CharField(max_length=20,
                            choices=UserType.choices,
                            default=UserType.USER,
                            )

    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['-username']

    @property
    def is_admin(self):
        return self.role == self.UserType.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == self.UserType.MODERATOR
