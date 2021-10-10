from django.db import models


class Sensor(models.Model):
    sensorId = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return f"sensor {self.sensorId}"
