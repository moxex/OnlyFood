from django.urls import path
from . import views
from accounts import views as AccountViews


urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('profile/', views.vprofile, name='vprofile'),
]