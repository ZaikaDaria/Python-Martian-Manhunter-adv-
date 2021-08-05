import factory
from . import models


class DealerFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'new car'
    email = 'test@mail.com'
    city_id = 1
    user_id = 1


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'
        name = 'Kyiv'
        country_id = 1


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'Ukraine'
    code = '804'