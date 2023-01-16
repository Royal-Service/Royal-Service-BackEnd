from .serializers import MyTokenObtainPairSerializer, RegisterSerializer,CustmerProfileSerializer,CraftsmanSerializer,CraftsmanProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model


from utils.permission import IsOwner
from .models import CustmerProfile as CustmerProfileModel, CraftsmanProfile

# Login View 
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# Register View 
class RegisterView(generics.CreateAPIView):
    User = get_user_model()

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#-----------------------Custmer--------------------#

class CustmerProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
     Custmer profile View : allowed get, update, delet  
    '''
    User = CustmerProfileModel
    queryset = User.objects.all()
    serializer_class = CustmerProfileSerializer
    #permission_classes = [IsOwner]

#-----------------------Craftsman--------------------#

class CraftsmanView(generics.ListAPIView):
    '''
    view list of Craftsman Profiles
    '''
    queryset = CraftsmanProfile.objects.all()
    serializer_class = CraftsmanSerializer

class CraftsmanProfileView(generics.RetrieveAPIView):
    '''
    view Craftsman Profile details
    '''
    queryset = CraftsmanProfile.objects.all()
    serializer_class = CraftsmanSerializer

class CraftsmanProfileEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    view Craftsman Profile details
    '''
    queryset = CraftsmanProfile.objects.all()
    serializer_class = CraftsmanProfileSerializer
    permission_classes = [IsOwner]























# from rest_framework import viewsets, permissions, generics, status
# from .serializers import UserSerializer, CraftsmanSerializer, BookingSerializer, ReviewSerializer
# from .models import User, Craftsman, Booking, Review
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.views import APIView
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt,csrf_protect 
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import authenticate, login

# from rest_framework import generics,permissions
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import status


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class CraftsmanViewSet(viewsets.ModelViewSet):
#     queryset = Craftsman.objects.all()
#     serializer_class = CraftsmanSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)

#     def perform_create(self, serializer):
#         password = serializer.validated_data.get("password")
#         hashed_password = make_password(password)
#         serializer.save(password=hashed_password)

# class LoginView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         user = authenticate(username=self.request.data['username'], password=self.request.data['password'])
#         if user is not None:
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)

