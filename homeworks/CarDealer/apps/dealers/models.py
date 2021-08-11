from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    city = models.ForeignKey('dealers.City', on_delete=models.CASCADE)
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name='dealers')
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dealer_detail', kwargs={'slug': self.user})


class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey('dealers.Country', on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40)
    code = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
