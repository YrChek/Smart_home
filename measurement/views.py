from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementCreateSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    """Создание данных в Sensor по POST или чтение по GET"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
    """Добавление измерения"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer


class DataView(RetrieveUpdateAPIView):
    """Получение или обновление данных по одному датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
