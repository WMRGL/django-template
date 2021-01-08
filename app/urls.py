from django.urls import include
from django.urls import path

from app import views

urlpatterns = [
    path('api/', include('app.routing')),
    path('', views.IndexView.as_view(), name='index'),
]
