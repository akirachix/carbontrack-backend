from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User
from factory.models import Factory



class UserModelTest(TestCase):
    def setUp(self):
        self.factory = Factory.objects.create(factory_name="Test Factory")
    def test_create_manager(self):
        user = User.objects.create_user(
            email="girmaayemebet@gmail.com",
            password="gideye506",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="manager"
        )
        self.assertEqual(user.email, "girmaayemebet@gmail.com")
        self.assertEqual(user.phone_number, "+251923232323")
        self.assertEqual(user.user_type, "manager")
        self.assertTrue(user.check_password("gideye506#"))
    def test_create_factory_manager(self):
        user = User.objects.create_user(
            email="factory@girmaayemebet.com",
            password="gideye506",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="factory",
            factory=self.factory
        )
        self.assertEqual(user.factory, self.factory)
    def test_factory_manager_without_factory_raises_error(self):
        user = User(
            email="nofactory@girmaayemebet.com",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="factory"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()
    def test_manager_with_factory_raises_error(self):
        user = User(
            email="wrongmanager@girmaayemebet.com",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="manager",
            factory=self.factory
        )
        with self.assertRaises(ValidationError):
            user.full_clean()
    def test_update_user(self):
        user = User.objects.create_user(
            email="update@girmaayemebet.com",
            password="gideye506",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="manager"
        )
        user.first_name = "Updated"
        user.save()
        self.assertEqual(User.objects.get(id=user.id).first_name, "Updated")
    def test_delete_user(self):
        user = User.objects.create_user(
            email="delete@girmaayemebet.com",
            password="gideye506",
            first_name="Emebet",
            last_name="Girmay",
            phone_number="+251923232323",
            user_type="manager"
        )
        user_id = user.id
        user.delete()
        self.assertFalse(User.objects.filter(id=user_id).exists())