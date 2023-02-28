from datetime import datetime

from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


class Address(models.Model):
    city = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, default=+380000000000)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.city}, {self.street}'


class Subscription(models.Model):
    #TODO visits counter

    NAMES = [
        ('4 trainings', '4 trainings'),
        ('8 trainings', '8 trainings'),
        ('12 trainings', '12 trainings'),
        ('unlimited', 'unlimited')

    ]
    subscription_number = models.CharField(max_length=8, default=00000000, blank=False)
    name = models.CharField(max_length=15, choices=NAMES)
    visits_count = models.IntegerField()
    is_active = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now, verbose_name="Expires", null=True, blank=True)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'

    def __str__(self):
        return self.subscription_number


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    birth_date = models.DateField(blank=False)
    phone_number = models.CharField(max_length=255, blank=False)
    subscription = models.ForeignKey(Subscription, blank=False, on_delete=CASCADE)
    registration_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.surname


class Gym(models.Model):
    #TODO status open/closed
    #working shedule
    address = models.ForeignKey(Address, blank=False, on_delete=CASCADE)
    customers = models.ManyToManyField(Customer, blank=True,)
    opened_at = models.DateTimeField(auto_now=True)



