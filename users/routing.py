from django.urls import path
from .consumers import WSConsumer
from .consumers import NewConsumer
ws_urlpatterns = [
    path('ws/some/', WSConsumer.as_asgi()),
    path('ws/many/', NewConsumer.as_asgi()),
    
]