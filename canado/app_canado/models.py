# import uuid
import uuid
from django.contrib.auth.models import Group

from django.contrib.auth import user_logged_in
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

class Usermanager(BaseUserManager):
    def create_user(self, email, password=True):
        if not email:
            raise ValueError('Vartotojas turi turėti el. paštą')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USER_TYPES = (
        ('vadybininkas', 'vadybininkas'),
        ('mechanikas', 'mechanikas'),
        ('dazytojas', 'dazytojas'),
        ('elektrikas', 'elektrikas'),
        ('saltkalvis', 'saltkalvis'),

    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='El. paštas',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=60, blank=False)
    surname = models.CharField(max_length=60, blank=False)
    phone = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    objects = Usermanager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

