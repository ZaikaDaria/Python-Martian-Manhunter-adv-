from django.test import TestCase

from apps.orders.tests.factories import OrderFactory


class OrdersListViewTestCase(TestCase):
    def setUp(self):
        self.car = OrderFactory()
        self.url = f'/order/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class OrderDetailViewTestCase(TestCase):
    def setUp(self):
        self.order = OrderFactory()
        self.url = f'/order/{self.order.id}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.email)

    def test_not_found(self):
        response = self.client.get('/order/1234567/')
        self.assertEqual(response.status_code, 404)


