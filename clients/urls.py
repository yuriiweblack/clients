from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('clients/', views.clients, name='clients'),
    path('clients/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
