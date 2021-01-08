from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets

from app.serializers import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # permissions.IsAuthenticated