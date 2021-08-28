import factory
from factory import fuzzy
from apps.dealers.models import *
from apps.accounts.tests.factories import UserFactory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = fuzzy.FuzzyText(length=16)


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = fuzzy.FuzzyText(length=16)
    country = factory.SubFactory(CountryFactory)


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dealer

    title = factory.Sequence(lambda n: f'dealer_{n}')
    email = factory.Sequence(lambda n: f'testemail{n}@mail.com')
    user = factory.SubFactory(UserFactory)
    city = factory.SubFactory(CityFactory)
