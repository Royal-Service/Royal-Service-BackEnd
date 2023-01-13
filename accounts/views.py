from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Craftsman, Craft, Customer, Booking
from django.http import JsonResponse
from django.views import View


class CraftsmanListView(ListView):
    model = Craftsman
    context_object_name = 'craftsmen'

class CraftsmanCreateView(CreateView):
    model = Craftsman
    fields = ['__all__']
    success_url = reverse_lazy('craftsman_list')

class CraftsmanUpdateView(UpdateView):
    model = Craftsman
    fields = ['__all__']
    success_url = reverse_lazy('craftsman_list')

class CraftsmanDeleteView(DeleteView):
    model = Craftsman
    success_url = reverse_lazy('craftsman_list')

class CreateCraftView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        craftsman_id = request.POST.get('craftsman')
        craftsman = Craftsman.objects.get(id=craftsman_id)
        craft = Craft.objects.create(name=name, description=description, craftsman=craftsman)
        return JsonResponse({'id': craft.id, 'name': craft.name, 'description': craft.description,'craftsman':craft.craftsman.name})
