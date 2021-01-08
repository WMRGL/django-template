from django.urls import include
from django.urls import path
from django.urls import re_path
from rest_framework import routers

from app import consumers
from app import endpoints


# Channels
websocket_urlpatterns = [
    re_path(r'ws/app/(?P<group_name>\w+)/$', consumers.AppConsumer.as_asgi())
]

# RESTful API
router = routers.DefaultRouter()
router.register('users', endpoints.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]