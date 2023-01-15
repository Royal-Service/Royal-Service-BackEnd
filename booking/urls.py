from django.urls import path
from .views import CreateBookingView, BookingRetrieveUpdateDestroyView,UserBookingView

urlpatterns = [
    path("", UserBookingView.as_view(), name="Booking_list"),

    path(
        "<int:pk>/",
        BookingRetrieveUpdateDestroyView.as_view(),
        name="visits_detail",
    ),
    path("create/",CreateBookingView.as_view(), name="create_Booking")
]