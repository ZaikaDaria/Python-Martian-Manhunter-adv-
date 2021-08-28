
from django.test import TestCase

from apps.cars.tests.factories import CarFactory


class CarsListViewTestCase(TestCase):
    def setUp(self):
        self.car = CarFactory()
        self.url = f'/cars/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class CarsDetailViewTestCase(TestCase):
    def setUp(self):
        self.car = CarFactory()
        self.url = f'/cars/{self.car.slug}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.number)

    def test_not_found(self):
        response = self.client.get('/cars/incorrect-slug/')
        self.assertEqual(response.status_code, 404)