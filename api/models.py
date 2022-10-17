from django.db import models

# Create your models here.

class Item(models.Model):
    sensor_id = models.CharField(max_length=64)
    e_data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sensor_id