from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Profile
from accounts.utils import send_notification

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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                mail_template = 'accounts/email/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }
                if self.is_approved == True:
                    #send notification email
                    mail_subject = 'Congratulations! Your Online Store has been approved.'
                    send_notification(mail_subject, mail_template, context)  
                else:
                    #send notification email
                    mail_subject = 'We are sorry! You are not eligible for publishing your products on our market place.'
                    send_notification(mail_subject, mail_template, context)


        return super(Vendor, self).save(*args, **kwargs)
