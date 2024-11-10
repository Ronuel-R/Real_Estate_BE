from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    api_secret_key = models.CharField(max_length=255, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)

    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        
    def __str__(self):
        return self.username