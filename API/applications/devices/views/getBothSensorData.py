from django.shortcuts import render
from ..models import *


def getBothSensorDataEndpoint(request):
    queryset = Measure.objects.values("PPM", "date").filter(sensor_id="S001");
    labels   = [entry["date"] for entry in queryset]
    sensor1  = [entry["PPM"] for entry in queryset]

    queryset = Measure.objects.values("PPM", "date").filter(sensor_id="S002");
    sensor2  = [entry["PPM"] for entry in queryset]

    return render(request, 'showBothData.html', {
        "labels":  labels,
        "sensor1": sensor1,
        "sensor2": sensor2,
    })
