import factory
from . import models


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'
    car_id = 1
    status = 'In progress'
    first_name = 'Daria'
    last_name = 'Zaika'
    email = 'email@gmail.com'
    phone = '+380000000000'