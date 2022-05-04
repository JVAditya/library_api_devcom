from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateAPIView.as_view()),
    path('<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('<str:key>/', views.BookNameListCreateView.as_view()),
]