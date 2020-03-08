from django.db import models


class CampItem(models.Model):
    name = models.CharField(max_length=200, blank=False)
    quantity = models.PositiveIntegerField(blank=False)
