

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import ReviewRating
from .serializers import ReviewSerializer
from accounts.models import CustmerProfile,CraftsmanProfile
from .serializers import CreateReviewRatingSerializer,ReviewRatingSerializer
from rest_framework.generics import CreateAPIView
from django.db.models import Avg, Count


class ReviewView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(custmer=self.request.user.custmerprofile, craftsman_id=request.data.get('craftsman'))
            return Response({"status": "Review created successfully!"}, status=status.HTTP_201_CREATED)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetReviewViewCraftsman(APIView):
    def get_average_rating(self, craftsman_id):
        reviews = ReviewRating.objects.filter(craftsman=craftsman_id)
        average_rating = reviews.aggregate(Avg('rating'))
        count = reviews.aggregate(Count('id'))
        return {'average_rating': average_rating, 'count': count}
    
    def get(self, request, craftsman_id):
        try:
            craftsman = CraftsmanProfile.objects.get(id=craftsman_id)
            reviews = ReviewRating.objects.filter(craftsman=craftsman)
            serializer = ReviewSerializer(reviews, many=True)
            average_rating =self.get_average_rating(craftsman_id)

            data = {
                'average_rating': average_rating,
                'reviews': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except CraftsmanProfile.DoesNotExist:
            return Response({"error": "Craftsman not found."}, status=status.HTTP_404_NOT_FOUND)


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




class ReviewRatingListCreateAPIView(generics.ListAPIView):
    # ListCreateAPIView


    def home(request):
        CraftsmanProfiles = CraftsmanProfile.objects.all().filter(is_available=True).order_by('created_date')

        # Get the reviews
        reviews = None
        for CraftsmanProfile in CraftsmanProfiles:
            reviews = ReviewRating.objects.filter(product_id=CraftsmanProfile.id, status=True)

        context = {
            'CraftsmanProfile': CraftsmanProfile,
            'reviews': reviews,
        }
        return  context
        
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewRatingSerializer