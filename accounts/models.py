from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import CustomUserManager

class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTMER = "CUSTMER", "Custmer"
        CRAFTSMAN = "CRAFTSMAN", "Craftsman"

    base_role = Role.ADMIN

    email = models.EmailField(unique=True) # changes email to unique and blank to false
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.role or self.base_role
            return super().save(*args, **kwargs)


# CUSTMER Profile


class CustmerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTMER)


class Custmer(User):

    base_role = User.Role.CUSTMER

    Custmer = CustmerManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Custmer)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created and instance.role == "CUSTMER":
        CustmerProfile.objects.create(user=instance)



class CustmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True,null=True)
    last_name = models.CharField(max_length=256, blank=True,null=True)
    phone = models.FloatField(blank=True,null=True)


    def __str__(self):
        return self.user.email


# ProfessionalProfile

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True,null=True)
    phone = models.FloatField(blank=True,null=True)
    location = models.CharField(max_length=255,default="Jordan")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

# CRAFTSMAN Profile


class CraftsmanManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CRAFTSMAN)


class Craftsman(User):

    base_role = User.Role.CRAFTSMAN

    Craftsman = CraftsmanManager()

    class Meta:
        proxy = True



class CraftsmanProfile(ProfessionalProfile):
    craft = models.CharField(max_length=256, blank=True,null=True)



@receiver(post_save, sender=Craftsman)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CRAFTSMAN":
        CraftsmanProfile.objects.create(user=instance)

















# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class UserManager(models.Manager):
#     pass
# class User(AbstractUser):
#     role = models.CharField(max_length=255, choices=[("customer", "customer"), ("Craftsman", "Craftsman")],default="customer")
#     objects = UserManager()

# class Craftsman(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     craft = models.CharField(max_length=255 , choices=[("HomeRepairs", "Home repairs"), ("Plumbing", "Plumbing Work"), ("Electrical", "electrical work"), ("Packing", "Moving and packing"), ("HVAC", "HVAC repair"), ("Carpentry", "Carpentry"), ("Painting", "Painting"),],default=None)
#     location = models.CharField(max_length=255,default="Jordan")
#     rating = models.FloatField(default=None)
#     def __str__(self):
#         return self.first_name + self.last_name

# class Booking(models.Model):
#     craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE, null=True,default=None)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,default=None)
#     serviceType = models.CharField(max_length=255, default='')
#     date = models.DateField()
#     price = models.FloatField()



#     def __str__(self):
#         return f"Booking on {self.date} by {self.user} for {self.craftsman.craft} made by {self.craftsman.user}"

# class Review(models.Model):
#     craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE,null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     rating = models.FloatField()
#     reviewText = models.TextField()
#     date = models.DateField


