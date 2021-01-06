from django.urls import re_path

from worklog import consumers


websocket_urlpatterns = [
    re_path(r'ws/worklog/(?P<room_name>\w+)/$', consumers.WorklogConsumer.as_asgi())
]