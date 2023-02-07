from django.urls import path

from data import views

urlpatterns = [
    path('gym/', views.GymAPIView.as_view(), name='gym-list'),
    path('customer/', views.CustomerAPIView.as_view(), name='customer-list'),
]