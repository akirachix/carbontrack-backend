from django.test import TestCase
from decimal import Decimal
from datetime import datetime, timedelta
from factory.models import EnergyEntry, Factory

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
