from datetime import datetime

from django.db import models


# Create your models here.
class chech_in(models.Model):
    room_number = models.CharField(max_length=10)
    amount_paid = models.CharField(max_length=10)
    occupant_name = models.CharField(max_length=50)
    occupant_email = models.EmailField(max_length=50)
    occupant_occupation = models.CharField(max_length=50)
    number_of_nights = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField(default='1997-12-2')

    def __str__(self):
        return f'Room {self.room_number}'
