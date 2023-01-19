from django.urls import path
from .views import ReviewView,ReviewViewEdit,ReviewDetailView,CreateReviewView

urlpatterns = [
    path('', ReviewView.as_view()),
    path('<int:pk>/', ReviewViewEdit.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path("create/", CreateReviewView.as_view(), name="create_review"), # just for admin if he want to booking 

]