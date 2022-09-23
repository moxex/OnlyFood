from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Profile

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, related_name='profile', on_delete=models.CASCADE)
    vendor_name = models.CharField(verbose_name=_('Vendor Name'), max_length=100)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modifid_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
