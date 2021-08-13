from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"