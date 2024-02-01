from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, date_of_birth, gender, email=None, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, date_of_birth, gender, email=None, password=None, **extra_fields):
        # Ensure the user is a superuser
        extra_fields.setdefault('is_superuser', True)

        # Call create_user method with superuser parameters
        return self.create_user(phone_number, date_of_birth, gender, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
    ]

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('gender', 'date_of_birth')

    def __str__(self):
        return self.email or self.phone_number

    @property
    def is_staff(self):
        return self.is_superuser

    @staticmethod
    def calculate_age(date_of_birth):
        # Assuming date_of_birth is in the format 'YYYY-MM-DD'
        birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
        current_date = datetime.now()

        # Calculate the difference in years
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

        return age
