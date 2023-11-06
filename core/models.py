from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title


class StarRating(models.IntegerChoices):
    ZERO = 0, 'Zero'
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'


class Review(models.Model):
    title = models.CharField(max_length=99, null=False, blank=False)
    stars = models.IntegerField(default=StarRating.FIVE, choices=StarRating.choices)
    content = models.TextField(max_length=500, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Product(models.Model):
    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=90, unique=True)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
