from django.urls import path
from .views import CreateBookingView, BookingRetrieveUpdateDestroyView, UserBookingView
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView, BookingSubmitAPIView
urlpatterns = [
    path("", UserBookingView.as_view(), name="Booking_list"),

    path(
        "<int:pk>/",
        BookingRetrieveUpdateDestroyView.as_view(),
        name="visits_detail",
    ),
    path("create/", CreateBookingView.as_view(), name="create_Booking"),
    path('bookings/', BookingListCreateAPIView.as_view(),
         name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(),
         name='booking-retrieve-update-destroy'),
    path('bookings/submit/', BookingSubmitAPIView.as_view(), name='booking-submit'),
]
