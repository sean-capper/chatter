from django.conf.urls import url

from . import consumer

websocket_urlpatterns = [
    url('ws/chat/', consumer.ChatConsumer)
]