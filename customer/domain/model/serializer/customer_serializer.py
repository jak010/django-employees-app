from django.db.models import Model
from rest_framework import serializers

from customer.domain import model


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Customers
        fields = '__all__'


class CustomerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Customers
        fields = '__all__'


class CustomerCreateSerializer(serializers.ModelSerializer):
    # customerName = serializers.CharField(max_length=50, required=True)
    # customerLastName = serializers.CharField(max_length=50, required=True)
    # customerFirstName = serializers.CharField(max_length=50, required=True)
    # phone = serializers.CharField(max_length=50, required=True)
    # addressLine1 = serializers.CharField(max_length=50, required=True)
    # addressLine2 = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = model.Customers
        fields = '__all__'
