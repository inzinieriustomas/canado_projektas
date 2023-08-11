from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Create your models here.
class auto(models.Model):
    title = models.CharField(
        max_length= 256)

    project_resume = models.CharField(
        max_length= 256)

    UTL_CHOICES = [
        ("Acura", "Acura"),
        ("Alfa Romeo", "Alfa"),
        ("Audi", "Audi"),
        ("Bentley", "Bentley"),
        ("BMW", "BMW"),
        ("Buick", "Buick"),
        ("Cadillac", "Cad"),
        ("Chevrolet", "Chev"),
        ("Chrysler", "Chrysler"),
        ("Citroen", "Citroen"),
        ("Dacia", "Dacia"),
        ("Dodge", "Dodge"),
        ('CSS', "CSS"),
        ('JS', "Java Script"),
        ('DK', 'Docker'),
        ('DJ', "Django"),
        ('JSON', "JSON"),
        ('HT ', "HTML"),
        ('TK ', "TKInter"),
        ('SQ', "SQlite"),
        ('API', "API"),
        ('WS', "Web Scraping"),
        ('GT', "Git"),
        ('GH', "GitHub")]
    UTL_CHOICES2 = [
        ("bak","bak")]
    Gamintojas = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    Marke = models.CharField(
        max_length=50,
        choices=UTL_CHOICES,
        blank=True)

    Variklis = models.CharField(
        max_length=20,
        choices=UTL_CHOICES2,
        blank=True)

    Galia = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    Spalva = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl5 = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl6 = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl7 = models.CharField(
        max_length=20,
        choices = UTL_CHOICES,
        blank=True)

    project_start_date = models.DateField(
        blank=False
    )
    project_image = models.ImageField(upload_to='images/', blank=True)

    PSTATUS_CHOICES = [
        ('K', "Kuriamas"),
        ('U', "Užbaigtas")]

    project_status = models.CharField(
        max_length= 1,
        choices= PSTATUS_CHOICES,
        blank=False
        )
    c_remarks = models.CharField(max_length=256, verbose_name='Pastabos', default='-')
    c_created_at = models.DateTimeField(auto_now_add=True)
    c_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title}, {self.project_resume}, {self.project_start_date}"


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
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
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
    objects = Usermanager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.name} {self.surname}"
    @property
    def is_staff(self):
        return self.is_admin






# class User(models.Model):
#     name = models.CharField(max_length=60, blank=False)
#     surname = models.CharField(max_length=60, blank=False)
#     email = models.EmailField(max_length=254, blank=False)
#     phone = models.CharField(max_length=12)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"