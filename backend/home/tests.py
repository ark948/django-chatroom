from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.

# client fixture is provided by pytest-django

@pytest.mark.django_db
def test_home_index_view(client):
    url = reverse('home:index')
    resposne = client.get(url)
    assert resposne.status_code == 200