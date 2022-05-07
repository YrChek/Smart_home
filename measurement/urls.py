from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from measurement.views import SensorView, MeasurementView, DataView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', DataView.as_view()),
]
