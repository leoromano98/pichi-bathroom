from django.db import models
from django.utils import timezone

class BathroomVisit(models.Model):
    place = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    deployed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['deployed_at']

    def __str__(self):
        return f"{self.place} - {self.deployed_at}"
