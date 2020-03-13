from django.db import models
from trips.models import CampingTrip



    
    
class CampItem(models.Model):
    name = models.CharField(max_length=200, blank=False)
    quantity = models.PositiveIntegerField(blank=False)
    trip = models.ForeignKey(to=CampingTrip, on_delete = models.CASCADE, null=False)
    
 
