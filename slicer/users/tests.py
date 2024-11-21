from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class RegistrationTestCase(TestCase):
    def test_registration_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)