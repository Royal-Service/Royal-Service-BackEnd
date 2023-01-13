from django.contrib import admin

# Register your models here.
from .models import Craftsman, Craft, Customer, Booking

admin.site.register([Craftsman,Craft,Customer,Booking])
