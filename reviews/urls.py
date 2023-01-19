from django.urls import path
from .views import ReviewView,ReviewViewEdit,ReviewDetailView

urlpatterns = [
    path('', ReviewView.as_view()),
    path('<int:pk>/', ReviewViewEdit.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

]