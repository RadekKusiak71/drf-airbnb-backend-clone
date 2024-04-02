from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404


class ReviewViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        queryset = Review.objects.all()
        queries = request.GET
        if 'reservation' in queries:
            queryset = queryset.filter(reservation=queries['reservation'])
        serialized_data = ReviewSerializer(queryset, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        review = get_object_or_404(Review, id=pk)
        serialized_data = ReviewSerializer(review, many=False).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        review = get_object_or_404(Review, id=pk)
        data = request.data
        serializer = ReviewSerializer(review, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        review = get_object_or_404(Review, id=pk)
        data = request.data

        serializer = ReviewSerializer(
            review, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        review = get_object_or_404(Review, id=pk)
        if request.user != review.review.user:
            return Response({"detail": "This review doesn\'t belong to this user."}, status=status.HTTP_401_UNAUTHORIZED)

        review.delete()
        return Response({"details": "Review deleted"}, status=status.HTTP_204_NO_CONTENT)
