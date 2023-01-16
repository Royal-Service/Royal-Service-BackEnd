# from tkinter.ttk import Style
from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from .models import Custmer, CustmerProfile, CraftsmanProfile, User
# from django.contrib.auth import authenticate


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):  # 2
        token = super().get_token(user)
        if user.role == "Craftsman":
            user_data = CraftsmanProfile.objects.get(user=user.id)
            token['info_id'] = user_data.id
        token['username'] = user.username

        return token

# Register a new user

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,  
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True,style={'input_type': 'password'})
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=User.Role.choices, required=True)

    class Meta:
        model = User
        fields = ('email','password', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop("password", None)
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        role = validated_data.pop('role')
        user = User.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name, role=role)
        if user.role == "CUSTMER":
            CustmerProfile.objects.create(user=user,first_name=first_name,last_name=last_name)
        elif  user.role == "CRAFTSMAN":
            CraftsmanProfile.objects.create(user=user,first_name=first_name,last_name=last_name)
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.set_password(password)
        instance.save()
        return instance

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(min_length=8, write_only=True, style={
#                                      'input_type': 'password'})
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     role = serializers.ChoiceField(choices=["CUSTMER", "CRAFTSMAN"])

#     class Meta:
#         model = User
#         fields = ('email', 'password', 'first_name', 'last_name', 'role')
#         extra_kwargs = {
#             "password": {'write_only': True}
#         }
#     def create(self, validated_data):
#         email = validated_data.pop('email')
#         password = validated_data.pop("password", None)
#         first_name = validated_data.pop('first_name')
#         last_name = validated_data.pop('last_name')
#         role = validated_data.pop('role')
#         user = User.objects.create_user(
#             email=email, password=password, first_name=first_name, last_name=last_name)
#         user.role = role
#         user.save()
#         return user

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     password = validated_data.pop("password", None)
    #     first_name = validated_data.pop('first_name')
    #     last_name = validated_data.pop('last_name')
    #     role = validated_data.pop('role')
    #     user = User.objects.create_user(
    #         email=email, password=password, first_name=first_name, last_name=last_name, role=role)

    #     instance = self.Meta.model(**validated_data)
    #     if instance is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

class CustmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustmerProfile
        fields = '__all__'

class CustmerProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = CustmerProfile
        fields = '__all__'
        extra_kwargs = {
            "password": {'write_only': True}
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
