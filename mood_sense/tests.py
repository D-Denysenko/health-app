from django.test import TestCase

from django.contrib.auth import get_user_model
from test_task.settings import MEDIA_ROOT
from os.path import join


class ValidateCoordinatesTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('danil2', 'freeforse@outlook.com', 'd82485761')
        self.client.login(username='change_login', password='change_password')

    def test_upload_photo_without_coordinates(self):
        with open(join(MEDIA_ROOT, 'mood', '2019', '10', '25', '2.jpeg'), 'rb') as file:
            response = self.client.post(
                path='/api/v1/mood/upload',
                data={
                    'profile': '1',
                    'characteristic': 'Happy',
                    'image': file,
                    'location': 'Lviv'
                }, follow=True)
        self.assertEqual(response.status_code, 201)


class AuthTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('danil2', 'freeforse@outlook.com', 'd82485761')

    def test_secure_page(self):
        response = self.client.post('/api/v1/mood/upload', follow=True)
        self.assertEqual(response.status_code, 403)


class ExampleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('aaaa', 'freeforse@outlook.com', 'd82485sss761')

    def test_secure_page(self):
        response = self.client.post('/api/v1/mood/upload', follow=True)
        self.assertEqual(response.status_code, 403)

