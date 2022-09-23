from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'vendor_name', 'is_approved', 'created_at']
    list_filter = ['user', 'vendor_name']

admin.site.register(Vendor,VendorAdmin)