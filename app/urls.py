from django.urls import path

from app import views
from app.routing import endpoint_urlpatterns

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
] + endpoint_urlpatterns
