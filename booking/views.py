from accounts.models import CustmerProfile, CraftsmanProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView

from .serializers import BookingSerializer,BookingDetailsSerializer,CreateBookingSerializer
from .models import Booking


class CreateBookingView(CreateAPIView):
    '''
    Create new book 
    '''
    queryset = Booking.objects.all()
    serializer_class = CreateBookingSerializer
    
    def perform_create(self, serializer):
        custmer = CustmerProfile.objects.get(user=self.request.user.id)

        return serializer.save(custmer=custmer)


class UserBookingView(ListAPIView):
    '''
    Get all bookings related for any user 
    '''
    def get_queryset(self):
        if self.request.user.role == 'CRAFTSMAN':
            craftsman = CraftsmanProfile.objects.get(user=self.request.user.id)
            data = Booking.objects.filter(craftsman=craftsman)
            return data

        elif self.request.user.role == 'CUSTMER':
            custmer = CustmerProfile.objects.get(user=self.request.user.id)
            data = Booking.objects.filter(custmer=custmer)
            return data

        else:
            return Booking.objects.all()
    serializer_class = BookingSerializer



class BookingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsCustmerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializer
   