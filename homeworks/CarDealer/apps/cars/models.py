from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class Car(models.Model):
    color = models.ForeignKey('cars.Color', on_delete=models.CASCADE)
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, null=True)
    model = models.ForeignKey('cars.Model', on_delete=models.CASCADE)
    engine_type = models.CharField(max_length=75, default=0)

    POLLUTANT_CLASS_A_PLUS = "A+"
    POLLUTANT_CLASS_A = "A"
    POLLUTANT_CLASS_B = "B"
    POLLUTANT_CLASS_C = "C"
    POLLUTANT_CLASS_D = "D"
    POLLUTANT_CLASS_E = "E"
    POLLUTANT_CLASS_F = "F"
    POLLUTANT_CLASS_G = "G"

    POLLUTANT_CLASS_CHOICES = (
        (POLLUTANT_CLASS_A_PLUS, "A+"),
        (POLLUTANT_CLASS_A, "A"),
        (POLLUTANT_CLASS_B, "B"),
        (POLLUTANT_CLASS_C, "C"),
        (POLLUTANT_CLASS_D, "D"),
        (POLLUTANT_CLASS_E, "E"),
        (POLLUTANT_CLASS_F, "F"),
        (POLLUTANT_CLASS_G, "G"),
    )
    pollutant_class = models.CharField(max_length=30, choices=POLLUTANT_CLASS_CHOICES, blank=True)
    price = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=75)

    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Selling Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    doors = models.SmallIntegerField(default=4)
    capacity = models.PositiveIntegerField(default=0)
    gear_case = models.CharField(max_length=75)
    number = models.CharField(max_length=30)
    slug = models.SlugField(max_length=75)
    sitting_place = models.PositiveSmallIntegerField(default=4)
    first_registration_date = models.DateTimeField()
    engine_power = models.PositiveIntegerField()
    picture = models.ForeignKey('cars.Picture', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.number


class Color(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color


class Brand(models.Model):
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.brand


class Model(models.Model):
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE)
    model = models.CharField(max_length=75)

    def __str__(self):
        return self.model


class Property(models.Model):

    CATEGORY_ECONOM = 'Econom'
    CATEGORY_COMFORT = 'Comfort'
    CATEGORY_BUSINESS = 'Business'

    CATEGORY_CHOICES = (
        (CATEGORY_ECONOM, 'Econom'),
        (CATEGORY_COMFORT, 'Comfort'),
        (CATEGORY_BUSINESS, 'Business'),
    )

    property = models.CharField(max_length=75)
    category = models.CharField(max_length=75, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return f'{self.property} {self.category}'


class CarProperty(models.Model):
    property_type = models.ForeignKey('cars.Property', on_delete=models.CASCADE)
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)

class Picture(models.Model):
    url = models.ImageField(upload_to='pictures', null=True, blank=True)
    position = models.IntegerField()
    metadata = models.TextField()

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'