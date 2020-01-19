from decimal import Decimal
from math import sin, cos, sqrt, atan2, radians

from django.db.models import Count
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import MoodSerializer


class MoodView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(id=self.kwargs['id']).first()
        moods = profile.moods.values('characteristic').annotate(total=Count('characteristic')).order_by()
        return Response(moods)


class ImageUpload(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = MoodSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        request._full_data = data

        return super().post(request, *args, **kwargs)


class CalculateProximity(APIView):
    permission_classes = (IsAuthenticated, )
    characteristic = 'Happy'

    @staticmethod
    def calculate_distance(first_latitude, first_longitude, second_latitude, second_longitude):
        """
        Calculate distance between two pairs of coordinates.

        :return: distance in kilometers.
        """
        R = 6373.0
        dlon = radians(second_longitude) - radians(first_longitude)
        dlat = radians(second_latitude) - radians(first_latitude)

        a = sin(dlat / 2) ** 2 + cos(radians(first_latitude)) * cos(radians(second_latitude)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(id=self.kwargs['id']).first()
        moods = profile.moods.filter(characteristic=self.characteristic)
        result = {}
        second_latitude = self.kwargs['latitude']
        second_longitude = self.kwargs['longitude']
        for mood in moods:
            if mood.latitude or mood.longitude:
                result[mood.location] = self.calculate_distance(
                    Decimal(mood.latitude), Decimal(mood.longitude), Decimal(second_latitude), Decimal(second_longitude)
                )

        return Response(result)



