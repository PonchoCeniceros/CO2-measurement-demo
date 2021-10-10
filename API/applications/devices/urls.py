from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homeEndpoint, name="home"),
    path("getSensorData/<str:sensorId>", views.getSensorDataEndpoint, name="get-sensor-data"),
    path("getBothSensorData/", views.getBothSensorDataEndpoint, name="get-both-sensor-data")
]
