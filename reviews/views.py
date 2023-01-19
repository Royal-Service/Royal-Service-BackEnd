

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import ReviewRating
from .serializers import ReviewSerializer
from accounts.models import CustmerProfile
from .serializers import CreateReviewRatingSerializer
from rest_framework.generics import CreateAPIView


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


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CreateReviewView(CreateAPIView):

    queryset = ReviewRating.objects.all()
    serializer_class = CreateReviewRatingSerializer
    
    def perform_create(self, serializer):
        custmer = CustmerProfile.objects.get(user=self.request.user.id)

        return serializer.save(custmer=custmer)
