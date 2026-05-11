from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'secret123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_signup_get(self):
        resp = self.client.get(reverse('core:signup'))
        self.assertEqual(resp.status_code, 200)

    def test_signin_get(self):
        resp = self.client.get(reverse('core:signin'))
        self.assertEqual(resp.status_code, 200)

    def test_home_requires_login_and_returns_200(self):
        # not logged in -> redirect to signin
        resp = self.client.get(reverse('core:home'))
        self.assertIn(resp.status_code, (302, 301))

        # login and try again
        logged = self.client.login(username=self.username, password=self.password)
        self.assertTrue(logged)
        resp = self.client.get(reverse('core:home'))
        self.assertEqual(resp.status_code, 200)
