from django.urls import path

from users import views


urlpatterns = [
    path(r'login', views.login, name='login'),
]
