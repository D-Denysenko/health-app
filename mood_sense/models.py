from GPSPhoto import gpsphoto
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from test_task.settings import MEDIA_ROOT


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Mood(models.Model):

    mood_characteristic = (
        ('Happy', 'Happy'),
        ('No pain', 'No pain'),
        ('Very mild', 'Very mild'),
        ('Discomforting', 'Discomforting'),
        ('Tolerable', 'Tolerable'),
        ('Distressing', 'Distressing'),
        ('Very distressing', 'Very distressing'),
        ('Intense', 'Intense'),
        ('Very intense', 'Very intense'),
        ('Utterly horrible', 'Utterly horrible'),
        ('Excruciating unbearable', 'Excruciating unbearable'),
        ('change_one', 'change_two')

    )
    profile = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE, related_name='moods', default=1)
    characteristic = models.CharField(choices=mood_characteristic, default='1', max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=18, blank=True, null=True)
    longitude = models.DecimalField(max_digits=21, decimal_places=18, blank=True, null=True)
    image = models.ImageField(upload_to='mood/%Y/%m/%d', null=True, blank=True)
    location = models.CharField(max_length=200, null=False, blank=False, default='Ukraine, Odessa')

    class Meta:
        index_together = ('latitude', 'longitude')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Mood)
def update_mood_instance(sender, instance, created, **kwargs):
    if created:
        photo = gpsphoto.GPSPhoto(MEDIA_ROOT + '/' + str(instance.image)).getGPSData()
        if photo:
            instance.latitude = photo['Latitude']
            instance.longitude = photo['Longitude']
            instance.save()


