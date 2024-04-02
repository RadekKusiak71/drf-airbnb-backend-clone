from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer, ProfileUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404


class UsersModelViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]

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
        profile = get_object_or_404(Profile, id=pk)
        serialized_data = ProfileSerializer(profile, many=False).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        profile = get_object_or_404(Profile, id=pk)
        data = request.data
        if profile:
            serializer = ProfileUpdateSerializer(profile, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        profile = get_object_or_404(Profile, id=pk)
        data = request.data
        serializer = ProfileUpdateSerializer(
            profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        profile = get_object_or_404(Profile, id=pk)
        profile.delete()
        return Response({"details": "Profile deleted"}, status=status.HTTP_204_NO_CONTENT)
