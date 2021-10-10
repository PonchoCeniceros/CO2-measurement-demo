from django.db import models
from .sensor import Sensor
from .location import Location


class Measure(models.Model):
    PPM = models.FloatField()
    humidity = models.FloatField(null=True)
    temperature = models.FloatField(null=True)
    date = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sensor.sensorId}: {self.PPM} PPM"
