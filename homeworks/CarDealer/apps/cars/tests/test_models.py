from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.dealers.tests.factories import *
from apps.cars.tests.factories import *
from apps.cars.models import *


class TestCarModel(TestCase):
    def setUp(self):
        self.dealer = DealerFactory()
        self.picture = PictureFactory()
        self.color = ColorFactory()
        self.model = ModelFactory()
        self.property = PropertyFactory()

    def test_model(self):
        car = Car.objects.create(
            number='AA 1234 AA',
            slug='23FF',
            engine_power=200,
            price=120000,
            capacity=2.0,
            dealer=self.dealer,
            picture=self.picture,
            color=self.color,
            model=self.model,
        )
        car.property.add(self.property)

        self.assertIsNotNone(car.id)
        self.assertEqual(str(car), 'AA 123 AA')
        self.assertEqual(car.number, '23FF')
        self.assertEqual(car.engine_power, 200)
        self.assertEqual(car.price, 120000)
        self.assertEqual(car.capacity, 2.0)
        self.assertEqual(car.doors, 4)
        self.assertEqual(car.sitting_place, 5)
        self.assertEqual(car.pollutant_type, Car.POLLUTANT_CLASS_CHOICES)
        self.assertEqual(car.status, Car.STATUS_CHOICES)


class TestPictureModel(TestCase):
    def test_model(self):
        picture = Picture.objects.create(
            position=10,
            metadata='metadata',
            url=SimpleUploadedFile(
                name='test.jpg',
                content=open('pictures/test.jpg', 'rb').read(),
                content_type='image/jpeg'
            )
        )

        self.assertIsNotNone(picture.id)
        self.assertIsNotNone(picture.url)
        self.assertEqual(picture.position, 10)
        self.assertEqual(picture.metadata, 'metadata')


class TestColorModel(TestCase):
    def test_model(self):
        color = Color.objects.create(
            name='Green',
        )

        self.assertIsNotNone(color.id)
        self.assertEqual(str(color), 'Green')


class TestModelOfCarModel(TestCase):
    def setUp(self) -> None:
        self.brand = BrandFactory()

    def test_model(self):
        model = Model.objects.create(
            name='Fabia',
            brand=self.brand,
        )

        self.assertIsNotNone(model.id)
        self.assertEqual(str(model), 'Fabia')


class TestBrandModel(TestCase):
    def test_model(self):
        brand = Brand.objects.create(
            name='Skoda',
        )

        self.assertIsNotNone(brand.id)
        self.assertEqual(str(brand), 'Skoda')


class TestPropertyModel(TestCase):
    def test_model(self):
        property = Property.objects.create(
            name='property',
        )

        self.assertIsNotNone(property.id)
        self.assertEqual(str(property), 'property')
        self.assertEqual(property.category, Property.CATEGORY_MIDSIZE)