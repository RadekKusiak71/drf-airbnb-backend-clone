from rest_framework import serializers, status
from .models import Review
from users.models import Profile
from rest_framework.response import Response


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        profile = self.validated_data["profile"]
        reservation_id = self.validated_data["reservation"]
        if Review.objects.filter(reservation=reservation_id, profile=profile).exists():
            raise serializers.ValidationError("You already posted a review")
        self.validated_data['profile'] = profile
        return super().create(validated_data)
