from django.shortcuts import render
from ..models import *


def getSensorDataEndpoint(request, sensorId):
    queryset = Measure.objects.values("PPM", "date").filter(sensor_id=sensorId);
    labels = [entry["date"] for entry in queryset]
    data = [entry["PPM"] for entry in queryset]

    return render(request, 'showData.html', {
        "labels": labels,
        "data": data,
    })

