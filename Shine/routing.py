from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
# from notifications.consumers import NotificationConsumer
from users.models import MessageConsumer

from .wsgi import *

# # Umair new
# import os
# import django
# from channels.routing import get_default_application


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "textology.settings")
# django.setup()
# application = get_default_application()

# # Umair new end



application = ProtocolTypeRouter({
    "websocket": URLRouter([
        # path("user/", NotificationConsumer),
        path("users/", MessageConsumer),
    ])
})




