from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from factory.models import MCU, Factory
from emissions.models import Emissions

class EmissionsAPITestCase(APITestCase):
    def setUp(self):
        self.factory = Factory.objects.create(factory_name="Test Factory")
        self.mcu = MCU.objects.create(mcu_id="MCU123", factory=self.factory)
        self.emission = Emissions.objects.create(
            device_id="MCU123",
            mcu=self.mcu,
            emission_rate= 0.234567890123456
        )
        self.list_url = reverse('emissions-list')  

    def test_create_emission(self):
        data = {
            "device_id": "MCU123",
            "emission_rate": 0.345678901234567
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Emissions.objects.count(), 2)

    def test_list_emissions(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

  

   


