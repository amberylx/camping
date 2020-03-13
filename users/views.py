from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse


class CampingLoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('inventory_list')


class CampingLogoutView(auth_views.LogoutView):
    def get_next_page(self):
        return reverse('login')
