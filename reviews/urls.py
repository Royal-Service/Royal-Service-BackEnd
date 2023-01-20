from django.urls import path
from .views import ReviewView,ReviewViewEdit,ReviewDetailView,CreateReviewView,ReviewRatingListCreateAPIView,GetReviewViewCraftsman

urlpatterns = [
    path('', ReviewView.as_view()), # post 
    path('craftsman/<int:craftsman_id>/', GetReviewViewCraftsman.as_view()), ## this route is to get the reviews for a specific craftsman
    path('<int:pk>/edit/', ReviewViewEdit.as_view()), #update
    path('<int:pk>', ReviewDetailView.as_view(), name='review-detail'), #get
    path("create/", CreateReviewView.as_view(), name="create_review"), #post
    path('reviews/', ReviewRatingListCreateAPIView.as_view(), name='all-review-detail'), #get all reviews

]