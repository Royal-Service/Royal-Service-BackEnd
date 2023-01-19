from django.db import models


# Create your models here.

class ReviewRating(models.Model):
    craftsman = models.ForeignKey('accounts.CraftsmanProfile', on_delete=models.CASCADE)
    custmer = models.ForeignKey('accounts.CustmerProfile', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject