from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )

    username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email Adress'), max_length=200, unique=True)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=20, blank=True)
    role = models.PositiveSmallIntegerField(verbose_name=_('Role'), choices=ROLE_CHOICE, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role



class Gender(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', 
                                    on_delete=models.CASCADE)
    profile_photo = models.ImageField(verbose_name=_('Profile Photo'), upload_to='users/profile_photos', 
                                        default='/profile_default.png', blank=True, null=True)
    cover_photo = models.ImageField(verbose_name=_('cover Photo'), upload_to='users/cover_photos', 
                                        blank=True, null=True)
    gender = models.CharField(verbose_name=_('Gender'), choices=Gender.choices, 
                                default=Gender.OTHER, max_length=20)
    address = models.CharField(verbose_name=_('Adress'), max_length=250, blank=True, null=True)
    country = models.CharField(verbose_name=_('Country'), default='Nigeria', max_length=100, blank=False, null=False)
    state = models.CharField(verbose_name=_('State'), default='Kano', max_length=50, blank=False, null=False)
    city = models.CharField(verbose_name=_('City'), max_length=180, 
                                default='Fagge', blank=False, null=False)
    latitude = models.CharField(verbose_name=_('Latitude'), max_length=20, blank=True, null=True)
    longitude = models.CharField(verbose_name=_('Longitude'), max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return f"{self.user.username}'s profile"
