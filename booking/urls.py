from django.urls import path
from .views import CreateBookingView
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView, BookingSubmitAPIView
urlpatterns = [
    # path("", UserBookingView.as_view(), name="Booking_list"),
#  BookingRetrieveUpdateDestroyView, UserBookingView
    # path(
    #     "<int:pk>/",
    #     BookingRetrieveUpdateDestroyView.as_view(),
    #     name="booking_detail",
    # ),
    path("create/", CreateBookingView.as_view(), name="create_Booking"),



    path('', BookingListCreateAPIView.as_view(),
         name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(),
         name='booking-retrieve-update-destroy'),
    path('bookings/submit/', BookingSubmitAPIView.as_view(), name='booking-submit'),
]
