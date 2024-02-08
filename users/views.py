from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer, ProfileUpdateSerializer


class UsersModelViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Profile.objects.all()
        queries = request.GET

        if queries:
            queryset = queryset.filter(
                user__username__contains=queries['username'])
        if queryset:
            serialized_data = ProfileSerializer(queryset, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        if queryset:
            serialized_data = ProfileSerializer(queryset, many=False).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ProfileUpdateSerializer(queryset, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        data = request.data
        if queryset:
            serializer = ProfileUpdateSerializer(
                queryset, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        if queryset:
            queryset.delete()
            return Response({"details": "Profile deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"details": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)