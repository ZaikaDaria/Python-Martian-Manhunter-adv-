from django.core.validators import RegexValidator
from django.db import models


class Order(models.Model):

    STATUS_IN_PROGRESS = 'In progress'
    STATUS_COMPLETED = 'Completed'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = (
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_REJECTED, 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_IN_PROGRESS)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = RegexValidator(regex=r'^\+?1?\d{8-15}$')
    message = models.TextField(blank=True)
    car = models.ForeignKey('cars.Cars', on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
