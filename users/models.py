from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', related_query_name='custom_user', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', related_query_name='custom_user', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'CustomUser'