from rest_framework import serializers
from .models import ReviewRating

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

