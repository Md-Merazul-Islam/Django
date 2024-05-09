from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand


class Car (models.Model):
    category = models.ManyToManyField(Brand)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='cars/media/uploads/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.car.name}'
