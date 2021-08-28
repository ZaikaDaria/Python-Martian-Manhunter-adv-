import factory
from factory import fuzzy
from apps.cars.models import *
from apps.dealers.tests.factories import DealerFactory


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color

    color = factory.Sequence(lambda n: f'color_{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    brand = factory.Sequence(lambda n: f'brand_{n}')


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    property = factory.Sequence(lambda n: f'property_{n}')


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Picture

    url = factory.django.ImageField(from_path='test.jpg')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Model

    model = factory.Sequence(lambda n: f'model_{n}')
    brand = factory.SubFactory(BrandFactory)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    number = 'AA1111AA'
    slug = factory.Sequence(lambda n: f'slug_{n}')
    model = factory.SubFactory(ModelFactory)
    engine_power = fuzzy.FuzzyInteger(10, 200)
    color = factory.SubFactory(ColorFactory)
    brand = factory.SubFactory(BrandFactory)
    dealer = factory.SubFactory(DealerFactory)
    picture = factory.SubFactory(PictureFactory)
