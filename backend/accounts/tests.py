from django.test import TestCase
import pytest

# Create your tests here.

from accounts.models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user('test01', 'test01@something.com', 'test123*A')
    assert CustomUser.objects.count() == 1