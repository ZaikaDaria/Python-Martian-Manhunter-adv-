from django.test import TestCase

from apps.dealers.tests.factories import CityFactory, CountryFactory
from apps.accounts.tests.factories import UserFactory
from apps.dealers.models import *


class TestDealerModel(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.city = CityFactory()

    def test_model(self):
        dealer = Dealer.objects.create(
            title='test dealer',
            email='testemail@mail.com',
            user=self.user,
            city=self.city,
        )

        self.assertIsNotNone(dealer.id)
        self.assertEqual(str(dealer.title), 'test dealer')
        self.assertEqual(dealer.email, 'testemail@mail.com')


class TestCityModel(TestCase):

    def setUpTestData(self) -> None:
        self.country = CountryFactory()
        self.city = CityFactory()

    def test_model(self):
        city = City.objects.create(name=self.city, country=self.country)

        self.assertIsNotNone(city.id)


class TestCountryModel(TestCase):
    def test_model(self):

        country = Country.objects.create(
            name=CountryFactory(),
            code='49',
        )

        self.assertIsNotNone(country.id)
        self.assertEqual(country.code, '49')
