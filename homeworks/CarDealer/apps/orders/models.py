from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse


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
    phoneNumberRegex = RegexValidator(regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=20, null=True)
    message = models.TextField(blank=True)
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'id': self.id})
