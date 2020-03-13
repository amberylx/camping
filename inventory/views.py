from django.shortcuts import render

from inventory import models


def inventory_list(request):
    camp_items = models.CampItem.objects.all()

    return render(request, 'inventory_list.html', {
        'camp_items': camp_items
    }, content_type='text/html')
