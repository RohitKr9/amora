from django.urls import path
from .views import roomView

urlpatterns = [
    path('room/', roomView, name='room'),
]
