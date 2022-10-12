from .models import Vendor

#Helper function to get a vendor
def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor