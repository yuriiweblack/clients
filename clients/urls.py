from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('clients/details/<int:id>', views.details, name='details')
]