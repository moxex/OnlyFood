from django.urls import path
from . import views


urlpatterns = [
    path('accounts/registerUser/', views.registerUser, name='registerUser')
]