# from tkinter.ttk import Style
from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from .models import Custmer,CustmerProfile, CraftsmanProfile, User as UserModel
# from django.contrib.auth import authenticate

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user): #2 
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        user_data =''
        if user.role == "Craftsman":
            user_data = CraftsmanProfile.objects.get(user=user.id)
        print(user_data,"user_datauser_data")
        token['info_id'] = user_data.id
        token['username'] = user.username

        return token

# Register a new user
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,  
            validators=[UniqueValidator(queryset=Custmer.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True,style={'input_type': 'password'})
    
    class Meta:
        model = Custmer
        fields = ('email','password')
        extra_kwargs = {
           "password" : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CustmerProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    print(user, "user in serrrr")
    class Meta:
        model = CustmerProfile
        fields = '__all__'
        extra_kwargs = {
           "password" : {'write_only': True}
        }

class CraftsmanSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CraftsmanProfile
        fields = '__all__'

class CraftsmanProfileSerializer(serializers.ModelSerializer):
  
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CraftsmanProfile
        fields = '__all__'













# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Craftsman, Booking, Review

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'role')
#         extra_kwargs = {'password': {'write_only': True}}

# class CraftsmanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Craftsman
#         fields = ('id', 'user', 'craft', 'location', 'rating')

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ('id', 'craftsman', 'user', 'serviceType', 'date', 'price')

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('id', 'craftsman', 'user', 'rating', 'reviewText', 'date')