from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registerUser/', views.registerUser, name='registerUser'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/myAccount/', views.myAccount, name='myAccount'),
    path('accounts/custDashboard/', views.custDashboard, name='custDashboard'),
    path('accounts/vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),
]