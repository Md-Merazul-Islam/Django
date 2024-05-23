from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    

class Book(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price =models.DecimalField(max_digits=10,decimal_places=2)
    purchase_history = models.ManyToManyField(User, through='Purchase')
    
    def __str__(self) :
        return self.title
    

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class purchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    