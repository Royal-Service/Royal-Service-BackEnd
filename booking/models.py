from django.db import models
from datetime import datetime
from accounts.models import CraftsmanProfile, CustmerProfile

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
)
class Booking(models.Model):
    """
    Booking model
    """
    custmer = models.ForeignKey(
        CustmerProfile, on_delete=models.CASCADE, related_name="custmer",blank=True,null=True
    )
    craftsman = models.ForeignKey(
        CraftsmanProfile, on_delete=models.CASCADE, related_name="craftsman",blank=True,null=True
    )
    description = models.TextField(blank=True,null=True,default="No description")
    created_at = models.DateField(auto_now_add=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"
        
    def __str__(self):
        return f"Booking on {self.day} at {self.time} from {self.custmer.first_name} for {self.craftsman.crafts} made by {self.craftsman.user.first_name}"