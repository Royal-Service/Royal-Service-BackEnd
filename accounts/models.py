from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import CustomUserManager

CRAFT = [('PLUMBING_WORK', 'plumbing Work'),
         ('ELECTRICAL_WORK', 'Electrical Work'),
         ('MOVING_AND_PACKING', 'Moving and packing'),
         ('HOME_REPAIRS', 'Home_Repairs'),
         ('POWER_WASHING', 'Power Washing'),
         ('PAINTING', 'Painting'),
         ('CARPENTRY', 'Carpentry'),
         ('HVAC_REPAIR', 'HVAC_repair'),]
locations = [
    ('AMMAN', 'Amman'),
    ('ZARQA', 'Zarqa'),
    ('BALQA', 'Balqa'),
    ('MADABA', 'Madaba'),
    ('KARAK', 'Karak'),
    ('IRBID', 'Irbid'),
    ('MAFRAQ', 'Mafraq'),
    ('JERASH', 'Jerash'),
    ('TAFILAH', 'Tafilah'),
    ('MAAN', "Ma'an"),
    ('AJLOUN', 'Ajloun'),
    ('AQAPA', 'Aqaba'),
]

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
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
    # phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    phone_number = models.CharField(max_length=11,blank=True, help_text='Contact phone number')
    location = models.CharField(max_length=50, choices=locations ,default='Amman',blank=True,null=True)
    crafts = models.CharField(max_length=50, choices=CRAFT ,default='Electrical Work',blank=True,null=True)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.role or self.base_role
    #         return super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.id:
            username = self.username
            username_exists = True
            counter = 1
            self.username = username
            while username_exists:
                try:
                    username_exists = User.objects.get(username=username)
                    if username_exists:
                        username = self.username + '_' + str(counter)
                        counter += 1
                except User.DoesNotExist:
                    self.username = username
                    break
        super(User, self).save(*args, **kwargs)


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


class CustmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True,null=True)
    last_name = models.CharField(max_length=256, blank=True,null=True)
    # phone = models.FloatField(blank=True,null=True)
    # phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    phone_number = models.CharField(max_length=11,blank=True, help_text='Contact phone number')
    location = models.CharField(max_length=50, choices=locations ,default='Amman',blank=True,null=True)


    def __str__(self):
        return self.user.email

@receiver(post_save, sender=Custmer)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created and instance.role == "CUSTMER":
        CustmerProfile.objects.create(user=instance)

# ProfessionalProfile

# class ProfessionalProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=256, blank=True,null=True)
#     # phone = models.FloatField(blank=True,null=True)
#     location = models.CharField(max_length=255,default="Jordan")

#     def __str__(self):
#         return self.user

#     class Meta:
#         abstract = True

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



class CraftsmanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True,null=True)
    last_name = models.CharField(max_length=256, blank=True,null=True)
    # phone = models.FloatField(blank=True,null=True)
    # phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    phone_number = models.CharField(max_length=11,blank=True, help_text='Contact phone number')
    crafts = models.CharField(max_length=50, choices=CRAFT ,default='Electrical Work',blank=True,null=True)
    # craft = models.CharField(max_length=256, blank=True,null=True)
    location = models.CharField(max_length=50, choices=locations ,default='Amman',blank=True,null=True)
    def __str__(self):
        return self.first_name



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

