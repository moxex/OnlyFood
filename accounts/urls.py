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
    path('accounts/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/forgot_password/', views.forgot_password, name='forgot_password'),
    path('accounts/reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, 
                                            name='reset_password_validate'),
    path('accounts/reset_password/', views.reset_password, name='reset_password'),
]