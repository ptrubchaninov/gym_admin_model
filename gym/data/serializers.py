from data.models import Gym, Customer, Address, Subscription
from rest_framework import serializers


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'
        read_only_fields = ('opened_at',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('registration_date',)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'