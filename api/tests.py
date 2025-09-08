from django.test import TestCase
from factory.models import Factory
from factory.models import MCU

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


