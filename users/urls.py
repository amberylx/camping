from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.CampingLoginView.as_view(), name='login')
]
