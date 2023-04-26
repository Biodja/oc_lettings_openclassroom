from django.test import TestCase
from django.urls import reverse
from Profiles.models import Profile
from django.contrib.auth.models import User

from django.test import TestCase


class LettingsTestCase(TestCase):

    def setUp(self) -> None:
        u = User.objects.create_user("HeadlinesGazer","aa@a.cdo","test")
        Profile.objects.create(favorite_city="LA", user=u)
        return super().setUp()

    def test_letting_index(self):
        uri = reverse('lettings_index')
        resp = self.client.get(uri)
        self.assertTrue('title' in str(resp.content))

    def test_profil_param(self):
        uri = reverse("lettings_index", kwargs={"lettingslettings": "Oceanview Retreat"})
        resp = self.client.get(uri)
        self.assertTrue('title' in str(resp.content))



"""import pytest

@pytest.mark.django_db
def test_index(client):
    print('eoeoeoeoe')
    uri = reverse('lettings:index')
    resp = client.get(uri)
    assert 'title' in str(resp.content)

"""