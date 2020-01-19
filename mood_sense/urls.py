from django.urls import path, include

from .views import MoodView, ImageUpload, CalculateProximity

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('mood/proximity/<int:id>/<str:latitude>/<str:longitude>', CalculateProximity.as_view(), name='calculate_proximity'),
    path('mood/<int:id>', MoodView.as_view(), name='frequency_distribution'),
    path('mood/upload', ImageUpload.as_view(), name='upload_mood_capture'),
]
