from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from marketplace import views as MarketplaceViews

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('marketplace/', include('marketplace.urls')),

    # CART
    path('cart/', MarketplaceViews.cart, name='cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Only Food Admin'
admin.site.site_title = 'Only Food Admin Portal'
admin.site.index_title = 'Welcome to the Only Food Portal'
