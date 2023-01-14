from rest_framework import serializers
from .models import Craftsman, Craft, Customer, Booking

class CraftsmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craftsman
        fields = ('name', 'phone', 'email', 'location')

class CraftSerializer(serializers.ModelSerializer):
    craftsman = serializers.PrimaryKeyRelatedField(queryset=Craftsman.objects.all())
    # craftsman = CraftsmanSerializer()
    class Meta:
        model = Craft
        fields = ('name', 'description', 'craftsman')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'location')

class BookingSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    craft = serializers.PrimaryKeyRelatedField(queryset=Craft.objects.all())
    class Meta:
        model = Booking
        fields = ('date', 'customer', 'craft', 'price')
