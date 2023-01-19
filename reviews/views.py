

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ReviewRating
from .serializers import ReviewSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
class ReviewView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(custmer=self.request.user.custmerprofile, craftsman_id=request.data.get('craftsman'))
            return Response({"status": "Review created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(custmer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(custmer=self.request.user)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]