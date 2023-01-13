from django.urls import path
from .views import CraftsmanListView, CraftsmanCreateView, CraftsmanUpdateView, CraftsmanDeleteView,CreateCraftView

urlpatterns = [
    path('craftsmen/', CraftsmanListView.as_view(), name='craftsman_list'),
    path('craftsmen/create/', CraftsmanCreateView.as_view(), name='craftsman_create'),
    path('craftsmen/<int:pk>/update/', CraftsmanUpdateView.as_view(), name='craftsman_update'),
    path('craftsmen/<int:pk>/delete/', CraftsmanDeleteView.as_view(), name='craftsman_delete'),
    path('create-craft/', CreateCraftView.as_view(), name='create_craft'),

]