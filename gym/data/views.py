from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView

from data.models import Gym, Customer
from data.serializers import GymSerializer, CustomerSerializer


class GymAPIView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


