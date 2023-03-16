from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_index(client):
    print('eoeoeoeoe')
    uri = reverse('lettings:index')
    resp = client.get(uri)
    assert 'title' in str(resp.content)

