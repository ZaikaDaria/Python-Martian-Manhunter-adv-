from django.test import TestCase

from apps.dealers.tests.factories import DealerFactory


class DealerViewTestCase(TestCase):

    def setUp(self):
        self.url = f'/dealers/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class DealerDetailViewTestCase(TestCase):
    def setUp(self):
        self.dealer = DealerFactory()
        self.url = f'/dealers/{self.dealer.id}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dealer.title)

    def test_not_found(self):
        response = self.client.get('/dealers/4325960645/')
        self.assertEqual(response.status_code, 404)
