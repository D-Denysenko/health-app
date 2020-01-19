from rest_framework import serializers

from .models import Mood


class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = ['profile', 'characteristic', 'latitude', 'longitude', 'image', 'location']
        read_only_fields = ['latitude', 'longitude']

