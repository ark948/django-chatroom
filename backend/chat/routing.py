from django.urls import path, include


from chat.consumer import ChatConsumer


websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]