from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListCreateAPIView.as_view()),
    path('<int:pk>/', views.StudentRetrieveDeleteAPIView.as_view()),
]