from django.urls import path

from inventory import views


urlpatterns = [
    path(r'', views.inventory_list, name='inventory_list'),
]
