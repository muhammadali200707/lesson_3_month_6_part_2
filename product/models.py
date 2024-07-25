from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
