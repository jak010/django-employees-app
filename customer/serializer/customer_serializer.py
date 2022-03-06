from rest_framework import serializers

from ..models import Customers


class CustomerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
