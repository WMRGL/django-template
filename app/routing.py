from django.urls import re_path

from app import consumers


websocket_urlpatterns = [
    re_path(r'ws/app/(?P<group_name>\w+)/$', consumers.AppConsumer.as_asgi())
]