from django.urls import reverse
from django.test import TestCase
import pytest
from django.contrib.auth import get_user_model

# Create your tests here.

from accounts.models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user('test01@something.com', 'test123*A')
    assert CustomUser.objects.count() == 1



@pytest.mark.django_db
def test_user_signup(client):
    url = reverse('accounts:signup')
    resposne = client.post(url, {
        'username': "testuser01@gmail.com",
        'password': "test123*A"
    })

    assert resposne.status_code == 200


    print(get_user_model().objects.all())
