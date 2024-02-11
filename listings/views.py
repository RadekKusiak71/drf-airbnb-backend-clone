from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from .utils import filter_listing_queryset
from rest_framework.authentication import TokenAuthentication


class ListingViewSets(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        queryset = Listing.objects.all()
        queries = request.GET
        if queries:
            queryset = filter_listing_queryset(queryset, queries)
        serialized_data = ListingSerializer(queryset, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Listing.objects.get(id=pk)
        if queryset:
            serialized_data = ListingSerializer(queryset, many=False).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Listing.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ListingSerializer(queryset, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Listing not found"})

    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Listing.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ListingSerializer(queryset, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Listing not found"})

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Listing.objects.get(id=pk)
        if queryset:
            queryset.delete()
            return Response({"details": "Listing deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"details": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)
