import factory
from . import models


class CarFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    color_id = 1
    dealer_id = 1
    engine_type = 1
    population_type = 1
    price = 20000
    status = 'pending'
    door = 4
    number = 'KO7624BI'
    slug = 'SMW'
    sitting_place = 4
    engine_power = 200


class ColorFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'white'


class ModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    brand_id = 1
    name = 'M5'


class PropertyFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    category = 'Business'
    property = 'Business'