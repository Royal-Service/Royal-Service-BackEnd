from rest_framework import serializers
from .models import ReviewRating
from accounts.serializers import CraftsmanProfileSerializer

class ReviewSerializer(serializers.ModelSerializer):
    craftsman = serializers.PrimaryKeyRelatedField(read_only=True)
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ReviewRating
        fields = '__all__'

class CreateReviewRatingSerializer(serializers.ModelSerializer):
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ReviewRating
        fields = '__all__'    

class ReviewRatingSerializer(serializers.ModelSerializer):
    custmer = serializers.PrimaryKeyRelatedField(read_only=True)
    craftsman = CraftsmanProfileSerializer()
    

    class Meta:
        model = ReviewRating
        fields = '__all__'

