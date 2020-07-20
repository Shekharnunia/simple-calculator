from django.contrib import admin
from django.urls import path

from calculator.views import CalculatorAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/', CalculatorAPIView.as_view())
]
