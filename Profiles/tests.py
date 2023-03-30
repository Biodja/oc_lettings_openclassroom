from django.test import TestCase
from django.urls import reverse
from Profiles.models import Profile
from django.contrib.auth.models import User

from django.test import TestCase

class ProfilesTestCase(TestCase):
    

    def setUp(self) -> None:
        u = User.objects.create_user("HeadlinesGazer","aa@a.cdo","test")
        Profile.objects.create(favorite_city="LA", user=u)
        return super().setUp()
        
    def test_letting_index(self):
        uri = reverse('lettings_index')
        resp = self.client.get(uri)
        self.assertTrue('title' in str(resp.content))

    def test_profil_param(self):
        uri = reverse("profile", kwargs={"username": "HeadlinesGazer"})
        resp = self.client.get(uri)
        self.assertTrue('title' in str(resp.content))