from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ("user",)
