from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterListAPIView.as_view())
]