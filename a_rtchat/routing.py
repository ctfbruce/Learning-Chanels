from django.urls import path
from .consumers import * # equivalent of views, but for websockets

websocket_urlpatterns = [
    
    path("ws/chatroom/<chatroom_name>", ChatroomConsumer.as_asgi())
    
    
]