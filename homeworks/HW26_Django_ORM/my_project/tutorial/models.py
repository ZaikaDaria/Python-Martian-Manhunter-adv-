from django.db import models

RESTAURANT_LIST = (
    ('VEA', 'VEA'),
    ('ANTICHI_SAPORI', 'Antichi Sapori'),
    ('GANBARA', 'Ganbara'),
    ('NOMA', 'Noma'),
    ('SATURNE', 'Saturne'),
)

COUNTRY_LIST = (
    ('HK', 'Hong Kong'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('DK', 'Denmark'),
    ('FR', 'France'),
)

POSITION_LIST = (
    ('CHEF', 'Chef'),
    ('WAITER', 'Waiter'),
    ('COOK', 'Cook'),
    ('CLEANER', 'Cleaner'),
    ('SOMMELIER', 'Sommelier'),
)

SEASON_LIST = (
    ('SEASON_WINTER', 'Winter'),
    ('SEASON_SPRING', 'Spring'),
    ('SEASON_SUMMER', 'Summer'),
    ('SEASON_AUTUMN', 'Autumn'),
)


class Country(models.Model):
    country_name = models.CharField(max_length=50, choices=COUNTRY_LIST)

    def __str__(self):
        return self.country_name


class Staff(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    position = models.TextField(null=False, blank=False, choices=POSITION_LIST)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.position}"


class Dish(models.Model):
    dish_name = models.TextField(max_length=50, null=False, blank=False)
    ingredients = models.TextField()
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=2, decimal_places=2)
    season = models.TextField(null=False, blank=False, choices=SEASON_LIST)

    def __str__(self):
        return f"{self.dish_name} {self.price}"


class Menu(models.Model):
    menu_name = models.CharField(max_length=64)
    list_of_dishes = models.ManyToManyField(Dish)
    season_dish = models.CharField(max_length=64, choices=SEASON_LIST)

    def __str__(self):
        return self.manu_name


class Restaurant(models.Model):
    name = models.CharField(max_length=50, choices=RESTAURANT_LIST)
    location = models.OneToOneField(Country, on_delete=models.CASCADE, null=False, blank=False)
    employees = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False, blank=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name



