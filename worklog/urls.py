from django.urls import path

from worklog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
