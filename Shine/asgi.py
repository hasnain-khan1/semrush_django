import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from users.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shine.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
# 