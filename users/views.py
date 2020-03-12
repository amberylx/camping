from django.shortcuts import render

from users import models


def login(request):
    return render(request, 'login.html', {
    }, content_type='text/html')
