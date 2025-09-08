from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from factory.models import MCU, Factory
from emissions.models import Emissions
from django.test import TestCase
from factory.models import Factory
from factory.models import MCU
from decimal import Decimal
from datetime import datetime, timedelta
from factory.models import EnergyEntry, Factory
from factory.models import Factory
from factory.models import MCU

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

  

class FactoryTest(TestCase):

    def test_factory_creation_and_Str(self):
        factory = Factory.objects.create(
            factory_name="Litein Tea Factory",
            factory_location= " Kiasara-Roret-Litein, Kericho County"
        )

        self.assertEqual(str(factory),"Litein Tea Factory")

        self.assertEqual(factory.factory_name,"Litein Tea Factory")
        self.assertEqual(factory.factory_location," Kiasara-Roret-Litein, Kericho County")

        self.assertIsNotNone(factory.created_at)


class MCUTest(TestCase):

    def test_factory_creation_and_Str(self):
        factory= Factory.objects.create(
            factory_name="Litein Tea Factory",
            factory_location= " Kiasara-Roret-Litein, Kericho County"
        )
        mcu=MCU.objects.create(
            mcu_id="ESP-litein",
            factory=factory,
            status="active"
        )

        self.assertEqual(str(mcu),"ESP-litein")

        self.assertEqual(mcu.mcu_id,"ESP-litein")
        self.assertEqual(mcu.factory, factory)
        self.assertEqual(mcu.status, "active")

        self.assertIsNotNone(factory.created_at)

class FactoryTest(TestCase):

    def test_factory_creation_and_Str(self):
        factory = Factory.objects.create(
            factory_name="Litein Tea Factory",
            factory_location= " Kiasara-Roret-Litein, Kericho County"
        )

        self.assertEqual(str(factory),"Litein Tea Factory")

        self.assertEqual(factory.factory_name,"Litein Tea Factory")
        self.assertEqual(factory.factory_location," Kiasara-Roret-Litein, Kericho County")

        self.assertIsNotNone(factory.created_at)


class MCUTest(TestCase):

    def test_factory_creation_and_Str(self):
        factory= Factory.objects.create(
            factory_name="Litein Tea Factory",
            factory_location= " Kiasara-Roret-Litein, Kericho County"
        )
        mcu=MCU.objects.create(
            mcu_id="ESP-litein",
            factory=factory,
            status="active"
        )

        self.assertEqual(str(mcu),"ESP-litein")

        self.assertEqual(mcu.mcu_id,"ESP-litein")
        self.assertEqual(mcu.factory, factory)
        self.assertEqual(mcu.status, "active")

        self.assertIsNotNone(factory.created_at)


class EnergyEntryCRUDTests(TestCase):
    def setUp(self):
        self.factory = Factory.objects.create(
            factory_name="Test Factory",
            factory_location="Test Location"
        )
        self.energy_entry1 = EnergyEntry.objects.create(
            factory=self.factory,
            energy_type='electricity',
            energy_amount=Decimal('100.00'),
            tea_processed_amount=Decimal('50.00')
        )
        self.energy_entry2 = EnergyEntry.objects.create(
            factory=self.factory,
            energy_type='diesel',
            energy_amount=Decimal('200.00'),
            tea_processed_amount=Decimal('100.00')
        )

    def test_create_energy_entry(self):
        self.assertEqual(self.energy_entry1.energy_type, 'electricity')
        self.assertEqual(self.energy_entry1.tea_processed_amount, Decimal('50.00'))

    def test_get_energy_entry(self):
        entry = EnergyEntry.objects.get(pk=self.energy_entry1.pk)
        self.assertEqual(entry.energy_type, 'electricity')

    def test_update_energy_entry(self):
        self.energy_entry1.energy_amount = Decimal('150.00')
        self.energy_entry1.save()
        self.energy_entry1.refresh_from_db()
        self.assertEqual(self.energy_entry1.energy_amount, Decimal('150.00'))

    def test_delete_energy_entry(self):
        pk = self.energy_entry1.pk
        self.energy_entry1.delete()
        with self.assertRaises(EnergyEntry.DoesNotExist):
            EnergyEntry.objects.get(pk=pk)

    def test_empty_energy_entry_list(self):
        EnergyEntry.objects.all().delete()
        self.assertEqual(EnergyEntry.objects.count(), 0)

    def test_get_co2_sum_by_factory_and_date(self):
        target_date = datetime.now().date()
        expected_sum = self.energy_entry1.co2_equivalent + self.energy_entry2.co2_equivalent
        actual_sum = EnergyEntry.get_co2_sum_by_factory_and_date(self.factory.pk, target_date)
        self.assertEqual(actual_sum, expected_sum)

    def test_get_tea_processed_sum_by_factory_and_date(self):
        target_date = datetime.now().date()
        expected_sum = self.energy_entry1.tea_processed_amount + self.energy_entry2.tea_processed_amount
        actual_sum = EnergyEntry.get_tea_processed_sum_by_factory_and_date(self.factory.pk, target_date)
        self.assertEqual(actual_sum, expected_sum)
