from django.test import TestCase
from account.models import User
from decimal import Decimal


class RegisterTestCase(TestCase):

    def setUp(self) -> None:
         user = User.objects.create(username='john', password='Test456.', email='john@gmail.com', balance=5000)

    def test_register(self) -> bool:
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@gmail.com' )
        self.assertEqual(user.password, 'Test456.' )
        self.assertEqual(user.balance, 5000 )

class TestSuperUser(TestCase):

    def test_create_superuser(self) -> bool:
        admin_user = User.objects.create_superuser('super_user','super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

