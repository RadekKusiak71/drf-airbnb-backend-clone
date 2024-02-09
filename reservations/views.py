from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .models import Reservation


class ReservationsViewSets(viewsets.ViewSet):

    def list(self, request):
        queryset = Reservation.objects.all()
        serialized_data = ReservationSerializer(queryset, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Reservation.objects.get(id=pk)
        if queryset:
            serialized_data = ReservationSerializer(queryset, many=False).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        queryset = Reservation.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ReservationSerializer(queryset, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Reservation not found"})

    def partial_update(self, request, pk=None):
        queryset = Reservation.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ReservationSerializer(
                queryset, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Reservation not found"})

    def destroy(self, request, pk=None):
        queryset = Reservation.objects.get(id=pk)
        if queryset:
            queryset.delete()
            return Response({"details": "Reservation deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"details": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND)
