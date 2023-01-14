from django.urls import path
from .views import CraftsmanListCreate, CraftsmanRetrieveUpdateDestroy, CraftListCreate, CraftRetrieveUpdateDestroy, CustomerListCreate, CustomerRetrieveUpdateDestroy, BookingListCreate, BookingRetrieveUpdateDestroy

urlpatterns = [
    path('craftsmen/', CraftsmanListCreate.as_view(),
         name='craftsman-list-create'),
    path('craftsmen/<int:pk>', CraftsmanRetrieveUpdateDestroy.as_view(),
         name='craftsman-detail'),
    path('crafts/', CraftListCreate.as_view(), name='craft-list-create'),
    path('crafts/<int:pk>', CraftRetrieveUpdateDestroy.as_view(), name='craft-detail'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>', CustomerRetrieveUpdateDestroy.as_view(),
         name='customer-detail'),
    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>', BookingRetrieveUpdateDestroy.as_view(),
         name='booking-detail'),
]
