from accounts.models import CustmerProfile, CraftsmanProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView

from .serializers import BookingSerializer,BookingDetailsSerializer,CreateBookingSerializer
from .models import Booking
from rest_framework.views import APIView

from rest_framework import generics,permissions,status


from datetime import datetime, timedelta
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

def isCraftsmanValid(craftsman):
    try:
        craftsman_obj = CraftsmanProfile.objects.get(pk=craftsman)
        print(craftsman_obj)
        if craftsman_obj:
            return True
        else:
            return False
    except:
        return False

class BookingListCreateAPIView(generics.ListAPIView):
    # ListCreateAPIView

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    # serializer_class = BookingSerializer
    serializer_class = BookingDetailsSerializer

    
class BookingSubmitAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        today = datetime.now()
        minDate = today.strftime('%Y-%m-%d')
        deltatime = today + timedelta(days=21)
        strdeltatime = deltatime.strftime('%Y-%m-%d')
        maxDate = strdeltatime

        day = request.data.get('day')
        # service = request.data.get('service')
        description= request.data.get('description')
        craftsman = request.data.get("Craftsman")
        time = request.data.get("time")
        # date = day
        existing_booking = Booking.objects.filter(day=day,time=time,craftsman=craftsman)

        # if service != None:
        if day <= maxDate and day >= minDate:
            # if date != 'Friday' :
                if isCraftsmanValid(craftsman):
                    if not existing_booking:
                        custmer_profile = CustmerProfile.objects.get(user=request.user)
                        craftsman_obj = CraftsmanProfile.objects.get(pk=craftsman)
                        booking = Booking.objects.create(
                            custmer=custmer_profile,
                            craftsman=craftsman_obj,
                            day=day,
                            time=time,
                            description=description
                        )
                        booking.save()
                        return Response({"status": "Booking created successfully!"}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"status": "The selected craftsman is not available at this time."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"status": "The selected craftsman is not valid."}, status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     return Response({"status": "This day is not available for booking."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "This date is not available for booking."}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({"status": "Please Select A Service!"}, status=status.HTTP_400_BAD_REQUEST)

class CreateBookingView(CreateAPIView):
    '''
    Create new booking 
    '''
    queryset = Booking.objects.all()
    serializer_class = CreateBookingSerializer
    
    def perform_create(self, serializer):
        custmer = CustmerProfile.objects.get(user=self.request.user.id)

        return serializer.save(custmer=custmer)


# class UserBookingView(ListAPIView):
#     '''
#     Get all bookings related for any user 
#     '''
#     def get_queryset(self):
#         if self.request.user.role == 'CRAFTSMAN':
#             craftsman = CraftsmanProfile.objects.get(user=self.request.user.id)
#             data = Booking.objects.filter(craftsman=craftsman)
#             return data

#         elif self.request.user.role == 'CUSTMER':
#             custmer = CustmerProfile.objects.get(user=self.request.user.id)
#             data = Booking.objects.filter(custmer=custmer)
#             return data

#         else:
#             return Booking.objects.all()
#     serializer_class = BookingSerializer



# class BookingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsCustmerOrReadOnly]
#     queryset = Booking.objects.all()
#     serializer_class = BookingDetailsSerializer



