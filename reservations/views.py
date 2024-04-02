from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework.authentication import TokenAuthentication


class ReservationsViewSets(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        queryset = Reservation.objects.all()
        serialized_data = ReservationSerializer(queryset, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        reservation = Reservation.objects.get(id=pk)
        if reservation:
            serialized_data = ReservationSerializer(
                reservation, many=False).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"details": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        reservation = Reservation.objects.get(id=pk)
        data = request.data
        if reservation:
            serializer = ReservationSerializer(reservation, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Reservation not found"})

    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        reservation = Reservation.objects.get(id=pk)
        data = request.data
        if reservation:
            serializer = ReservationSerializer(
                reservation, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Reservation not found"})

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        reservation = Reservation.objects.get(id=pk)
        if reservation:
            reservation.delete()
            return Response(
                {"details": "Reservation deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"details": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND
            )
