from django.db.models import Model
from rest_framework import serializers

from customer.models import Customers


class CustomerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class CustomerCreateSerializer(serializers.ModelSerializer):
    # customerName = serializers.CharField(max_length=50, required=True)
    # customerLastName = serializers.CharField(max_length=50, required=True)
    # customerFirstName = serializers.CharField(max_length=50, required=True)
    # phone = serializers.CharField(max_length=50, required=True)
    # addressLine1 = serializers.CharField(max_length=50, required=True)
    # addressLine2 = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Customers
        fields = '__all__'
