from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
# Create your tests here.


class GymAPITestCase(APITestCase):
    def test_get(self):
        url = reverse('gym-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


