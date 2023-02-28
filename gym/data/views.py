from datetime import datetime

from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from data.models import Gym, Customer, Address, Subscription
from data.permisions import IsAdminOrReadOnly
from data.serializers import GymSerializer, CustomerSerializer, AddressSerializer, SubscriptionSerializer


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# class SubscriptionAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     #TODO visit counter(date list add date while expires quantity)
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer

    #try to equal expiration day with day today
    # def expires_at(self, due_date, is_active):
    #     day_today = datetime.now()
    #     self.due_date = Subscription.due_date()
    #     self.is_active = Subscription.is_active()
    #     if day_today == self.due_date:
    #         self.is_active = False


    # def expires_at(self, request, *args, **kwargs):
    #     day_today = datetime.now()
    #     due_date = request.GET.get('due_date', None)
    #     is_active = request.GET.get('is_active', None)
    #     if day_today == due_date:
    #         is_active = False

    # from django.conf import settings
    # from django.db import models
    # from django.utils import timezone
    # class Project(models.Model):
    #     date_start = models.DateTimeField(blank=True, null=True)
    #     date_end = models.DateTimeField(blank=True, null=True)
    #
    # def diff_date(self):
    #     return (self.date_end - self.date_start).days
    # self.proekt_end is None:
    # return (self.proekt_end.date() - self.proekt_start.date()).days

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

