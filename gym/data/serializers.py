from data.models import Gym, Customer
from rest_framework import serializers


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'
        read_only_fields = ('address', 'customers',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('surname', 'name ', 'phone_number', 'subscription')