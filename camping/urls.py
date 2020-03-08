from django.urls import include, path

from inventory import views


urlpatterns = [
    # path('inventory/', include('inventory.urls')),
    path(r'inventory/', views.inventory_list, name='inventory_list'),
]
