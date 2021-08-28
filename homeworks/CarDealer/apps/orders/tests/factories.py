import factory
from apps.orders.models import *
from apps.cars.tests.factories import CarFactory
from factory import fuzzy


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    status = factory.Sequence(lambda n: f'first name_{n}')
    first_name = factory.Sequence(lambda n: f'first name_{n}')
    last_name = factory.Sequence(lambda n: f'last name_{n}')
    email = factory.Sequence(lambda n: f'email{n}@mail.com')
    phone = '+380630000000'
    message = fuzzy.FuzzyText()
    car = factory.SubFactory(CarFactory)

