from django.test import TestCase
from apps.cars.tests.factories import CarFactory
from apps.orders.models import *


class TestOrderModel(TestCase):
    def setUp(self):
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Some',
            last_name='Name',
            email='test@mail.com',
            phone='+380630000000',
            message='some message',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Some Name')
        self.assertEqual(order.email, 'test@mail.com')
        self.assertEqual(order.phone, '+380630000000')
        self.assertEqual(order.message, 'some message')