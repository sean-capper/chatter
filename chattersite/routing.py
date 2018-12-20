from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatter.routing

application = ProtocolTypeRouter({
    # empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatter.routing.websocket_urlpatterns
        )
    )
})