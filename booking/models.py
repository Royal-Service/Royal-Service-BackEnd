from django.db import models
from accounts.models import CraftsmanProfile, CustmerProfile
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
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"
        
    def __str__(self):
        return self.description