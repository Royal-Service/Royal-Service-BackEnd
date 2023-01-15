from rest_framework import serializers

from accounts.serializers import CraftsmanProfileSerializer
from .models import Booking
from accounts.models import CraftsmanProfile

class BookingSerializer(serializers.ModelSerializer):
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)
    craftsman = CraftsmanProfileSerializer()
    class Meta:
        model = Booking
        fields = '__all__'

class CreateBookingSerializer(serializers.ModelSerializer):
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'    

class BookingDetailsSerializer(serializers.ModelSerializer):
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)
    craftsman = CraftsmanProfileSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
        