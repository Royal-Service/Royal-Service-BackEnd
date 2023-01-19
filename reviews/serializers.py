from rest_framework import serializers
from .models import ReviewRating
from accounts.serializers import CraftsmanProfileSerializer,CustmerProfileSerializer
class ReviewSerializer(serializers.ModelSerializer):
    craftsman = serializers.PrimaryKeyRelatedField(read_only=True)
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ReviewRating
        fields = '__all__'