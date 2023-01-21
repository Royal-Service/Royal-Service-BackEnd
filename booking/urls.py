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
    # just for admin if he want to booking
    path("create/", CreateBookingView.as_view(), name="create_Booking"),



    path('', BookingListCreateAPIView.as_view(),  # to get all booking list
         name='booking-list-create'),
    path('<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(),
         name='booking-retrieve-update-destroy'),  # you can use it  get  update and  delete
    path('submit/', BookingSubmitAPIView.as_view(), name='booking-submit'),
]
