from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    guests = models.IntegerField()
    food_preference = models.CharField(max_length=50)
    requirements = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Create your models here.
