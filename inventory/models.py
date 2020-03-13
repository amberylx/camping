from django.db import models


class CampingTrip(models.Model):
    start_date = models.DateField(name='start_date') 
    end_date = models.DateField(name='end_date')
    name = models.CharField(max_length=100, blank=True)
    park_name = models.CharField(max_length=100)
    #camp_item = models.ForeignKey(to=CampItem, on_delete=models.CASCADE, null=False) 
    
    
class CampItem(models.Model):
    name = models.CharField(max_length=200, blank=False)
    quantity = models.PositiveIntegerField(blank=False)
    trip = models.ForeignKey(to=CampingTrip, on_delete = models.CASCADE, null=False)
    
 
