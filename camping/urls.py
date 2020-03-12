from django.urls import include, path

from inventory import views


urlpatterns = [
    path('inventory/', include('inventory.urls')),
    path('users/', include('users.urls')),
]
