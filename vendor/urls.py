from django.urls import path
from . import views


urlpatterns = [
    path('vendors/registerVendor/', views.registerVendor, name='registerVendor')
]