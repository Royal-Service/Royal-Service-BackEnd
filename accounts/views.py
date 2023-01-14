from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Craftsman, Craft, Customer, Booking
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework import permissions
from .models import Craftsman, Craft, Customer, Booking
from .serializers import CraftsmanSerializer, CraftSerializer, CustomerSerializer, BookingSerializer

class CraftsmanListCreate(generics.ListCreateAPIView):
    queryset = Craftsman.objects.all()
    serializer_class = CraftsmanSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CraftsmanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Craftsman.objects.all()
    serializer_class = CraftsmanSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CraftListCreate(generics.ListCreateAPIView):
    queryset = Craft.objects.all()
    serializer_class = CraftSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CraftRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Craft.objects.all()
    serializer_class = CraftSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]












































# except ObjectDoesNotExist:
# @csrf_exempt
# def create_booking(request):
#     if request.method == 'POST':
#         data = request.POST
#         customer_name = data.get('customer_name')
#         customer_email = data.get('customer_email')
#         customer_phone = data.get('customer_phone')
#         customer_location = data.get('customer_location')
#         craft_name = data.get('craft_name')
#         date = data.get('date')
#         price = data.get('price')
#         try:
#             craft = Craft.objects.get(name=craft_name)
#             customer = Customer.objects.create(
#                 name=customer_name, email=customer_email,
#                 phone=customer_phone, location=customer_location
#             )
#             booking = Booking.objects.create(
#                 date=date, customer=customer, craft=craft, price=price
#             )
#             return JsonResponse({"status": "success"})
#         except Exception as e:
#             return JsonResponse({"status": "failed", "error": str(e)})
#     else:
#         return JsonResponse({"status": "failed", "error": "Invalid request method"})
# @csrf_exempt
# def create_craft(request):
#     form=OrderForm()
#     if request.method == 'POST':

#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         craftsman_id = request.POST.get('craftsman')
#         form = OrderForm(request.POST)
        
#         if form.is_valid():
#             form.save
        
#             # return JsonResponse({"error": "Craftsman with this id does not exist"})
#         craft = Craft.objects.create(name=name, description=description, craftsman=craftsman_id)
#         data = {'id': craft.id, 'name': craft.name, 'description': craft.description,'craftsman':craft.craftsman.name}
#         return JsonResponse(data)
#     return JsonResponse({"error": "Invalid request method"})

# def create_craft(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         craftsman_id = request.POST.get('craftsman')
#         craftsman = Craftsman.objects.get(id=craftsman_id)
#         craft = Craft.objects.create(name=name, description=description, craftsman=craftsman)
#         data = {'id': craft.id, 'name': craft.name, 'description': craft.description,'craftsman':craft.craftsman.name}
#         return JsonResponse(data)
#     return JsonResponse({"error": "Invalid request method"})
# class CraftsmanListView(ListView):
#     model = Craftsman
#     context_object_name = 'craftsmen'

# class CraftsmanCreateView(CreateView):
#     model = Craftsman
#     fields = ['__all__']
#     success_url = reverse_lazy('craftsman_list')

# class CraftsmanUpdateView(UpdateView):
#     model = Craftsman
#     fields = ['__all__']
#     success_url = reverse_lazy('craftsman_list')

# class CraftsmanDeleteView(DeleteView):
#     model = Craftsman
#     success_url = reverse_lazy('craftsman_list')

# class CreateCraftView(View):
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         craftsman_id = request.POST.get('craftsman')
#         craftsman = Craftsman.objects.get(id=craftsman_id)
#         craft = Craft.objects.create(name=name, description=description, craftsman=craftsman)
#         return JsonResponse({'id': craft.id, 'name': craft.name, 'description': craft.description,'craftsman':craft.craftsman.name})
