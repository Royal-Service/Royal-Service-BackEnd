from django.contrib.auth.models import AbstractUser

from django.db import models

class Craftsman(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10, null=True)
    email = models.EmailField(max_length=255,null=True)
    location = models.CharField(max_length=255,default="Jordan")
    def __str__(self):
        return self.name
        

class Craft(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE, related_name='craftsman')
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(max_length=10)
    location = models.CharField(max_length=255,default="Jordan")
    def __str__(self):
        return self.name

class Booking(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    craft = models.ForeignKey(Craft, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2 ,default=1)
    
    @property
    def craftsman_name(self):
        return self.craft.craftsman.name

    def __str__(self):
        return f"Booking on {self.date} by {self.customer.name} for {self.craft.name} made by {self.craft.craftsman.name}"