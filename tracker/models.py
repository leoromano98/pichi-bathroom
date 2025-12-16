from django.db import models

class BathroomVisit(models.Model):
    place = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.place} - {self.timestamp}"
