from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Craftsman
        fields ="__all__"
